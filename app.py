from flask import Flask

from flask_context_manager import ContextManager

app = Flask(__name__)
ContextManager.append(app)

if __name__ == '__main__':
    ContextManager.start(debug=True)
