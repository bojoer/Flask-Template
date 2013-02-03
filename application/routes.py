from flask import Blueprint

def setupRoutingRules(name, rules, bluePrintName=__name__, template_folder='templates'):
    bluePrint = Blueprint(name, bluePrintName, template_folder=template_folder)
    for url, view_func, methods in rules:
        bluePrint.add_url_rule(url, view_func=view_func, methods=methods)
    return bluePrint

def register_blueprints(app):
    from application.views.posts import listAll, single
    
    postRules = [
        ('/',           listAll,      ['GET', 'POST']),
        ('/<slug>/',    single,       ['GET', 'POST']),
    ]  
    
    app.register_blueprint(setupRoutingRules('posts', postRules), url_prefix='/posts')
    
