
from main import app

if __name__ == "__main__":
         if app.debug:
                app.run()
        else:
                gunicorn = WSGIApplication()
                gunicorn.load_wsgiapp = lambda: app
                gunicorn.cfg.set('bind', '%s:%s' % (host, port))
                gunicorn.cfg.set('workers', workers)
                gunicorn.cfg.set('threads', workers)
                gunicorn.cfg.set('pidfile', None)
                gunicorn.cfg.set('worker_class', 'sync')
                gunicorn.cfg.set('keepalive', 10)
                gunicorn.cfg.set('accesslog', '-')
                gunicorn.cfg.set('errorlog', '-')
                gunicorn.cfg.set('reload', True)
                gunicorn.chdir()
                gunicorn.run()
