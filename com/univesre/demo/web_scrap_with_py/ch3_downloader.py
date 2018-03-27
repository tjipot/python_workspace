class Downloader:
    def __init__(self, delay=5, user_agent='wswp', proxies=None, num_retries=1, cache=None):
        self.throttle = Throttle(delay);









class Throttle:
    """Throttle downloading by sleeping between requests to same domain"""
    def __init__(self, delay):
        pass