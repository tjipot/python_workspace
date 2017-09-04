#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Web App Structure @Nov 08, 2016 @HYE
# 此Web App的模型基础是acyncio的: 异步IO;
import logging;logging.basicConfig(level=logging.INFO) # 设置程序调试的等级为INFO;
import asyncio, os, json, time # 直接导入4个模块(文件);
from datetime import datetime  # 导入datetime模块(文件)的datetime类;
from aiohttp import web        # 导入aiohttp模块(文件)的web类;

from jinja2 import Environment, FileSystemLoader
import orm
from coreweb import add_routes, add_static

def init_jinja2(app, **kw):
	logging.info('init jinja2...')
	options = dict(
		autoescape = kw.get('autoescape', True),
		block_start_string = kw.get('block_start_string', '{%'),
		block_end_string = kw.get('block_end_string', '%}'),
		variable_start_string = kw.get('variable_start_string', '{{'),
		variable_end_string = kw.get('variable_end_string', '}}'),
		auto_reload = kw.get('auto_reload', True)
	)
	path = kw.get('path', None)
	if path is None:
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
	logging.info('set jinja2 template path: %s' % path)
	env = Environment(loader=FileSystemLoader(path), **options)
	filters = kw.get('filters', None)
	if filters is not None:
		for name, f in filters.items():
			env.filters[name] = f
	app['__templating__'] = env


# middleware
async def logger_factory(app, handler):
	async def logger(request):
		logging.info('Request: %s %s' % (request.method, request.path))
		# await asyncio.sleep(0.3)
		return (await handler(request))
	return logger

async def data_factory(app, handler):
	async def parse_data(request):
		if request.method == 'POST':
			if request.content_type.startswith('application/json'):
				request.__data__ = await request.json()
				logging.info('request json: %s' % str(request.__data__))
			elif request.content_type.startswith('application/x-www-form-urlencoded'):
				request.__data__ = await request.post()
				logging.info('request form: %s' % str(request.__data__))
		return (await handler(request))
	return parse_data

async def response_factory(app, handler):
	async def response(request):
		logging.info('Response handler...')
		r = await handler(request)
		if isinstance(r, web.StreamResponse):
			return r
		if isinstance(r, bytes):
			resp = web.Response(body=r)
			resp.content_type = 'application/octet-stream'
			return resp
		if isinstance(r, str):
			if r.startswith('redirect:'):
				return web.HTTPFound(r[9:])
			resp = web.Response(body=r.encode('utf-8'))
			resp.content_type = 'text/html;charset=utf-8'
			return resp
		if isinstance(r, dict):
			template = r.get('__template__')
			if template is None:
				resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
				resp.content_type = 'application/json;charset=utf-8'
				return resp
			else:
				resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
				resp.content_type = 'text/html;charset=utf-8'
				return resp
		if isinstance(r, int) and r >= 100 and r < 600:
			return web.Response(r)
		if isinstance(r, tuple) and len(r) == 2:
			t, m = r
			if isinstance(t, int) and t >= 100 and t < 600:
				return web.Response(t, str(m))
		# default:
		resp = web.Response(body=str(r).encode('utf-8'))
		resp.content_type = 'text/plain;charset=utf-8'
		return resp
	return response

def datetime_filter(t):
	delta = int(time.time() - t)
	if delta < 60:
		return u'1分钟前'
	if delta < 3600:
		return u'%s分钟前' % (delta // 60)
	if delta < 86400:
		return u'%s小时前' % (delta // 3600)
	if delta < 604800:
		return u'%s天前' % (delta // 86400)
	dt = datetime.fromtimestamp(t)
	return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

# def index(request):
# 	# 返回的数据要当做二进制字节数据处理: web类Response方法body参数;
# 	return web.Response(body=b'<h1>UNIVESRE</h1>', content_type='text/html', charset='utf-8')
# 
# 异步IO协程处理机制
# @asyncio.coroutine
async def init(loop):
	await orm.create_pool(loop = loop, host="127.0.0.1", post=3306, user="www", password="www", db="univesre")
	app = web.Application(loop=loop, middlewares=[logger_factory, response_factory]) # 传进异步事件loop对象;
	init_jinja2(app, filters=dict(datetime=datetime_filter))
	add_routes(app, 'handler')
	add_static(app)
	# app.router.add_route('GET', '/', index)		# add_route方法: 调用index(), 对首页"/"进行响应;
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)	# 产生一个服务: 在127.0.0.1地址和9000端口上, 这应该都是托aiohttp模块福吧(对指定网址路径, 指定网络地址进行响应);
	logging.info('Server started at http://127.0.0.1:9000...')		# 调试信息为INFO等级, 输出到终端..;
	return srv 									# 返回srv: 啥意思, 就是index()的返回了, 那个html label, 没错!;

loop = asyncio.get_event_loop() 		# asyncio模块: 产生异步事件loop对象;
loop.run_until_complete(init(loop))		# loop对象: init(loop);
loop.run_forever()						# loop对象: run forever;

# Web Framework Finished: Add More Features If You Want;