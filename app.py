# Starter Flask app placeholder with routes to be expanded.
from flask import Flask
app=Flask(__name__)
@app.get('/')
def home(): return 'Employee Management Starter'
if __name__=='__main__': app.run(debug=True)
