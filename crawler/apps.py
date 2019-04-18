from django.apps import AppConfig


class CrawlerConfig(AppConfig):
    name = 'crawler'

    def ready(self):
        import crawler.signals
