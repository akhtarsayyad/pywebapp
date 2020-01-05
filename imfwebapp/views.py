from django.shortcuts import render
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpRequest
from django.db import connection
def index(request):
    now = datetime.now()

    return render(
        request,
        "imfwebapp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "IMF",
            'message' : "Hello Akhtar!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
        )
def submit_form(req: HttpRequest) -> HttpResponse:
    now = datetime.now()
    cursor = connection.cursor()
    fname = req.GET['firstname']
    lname = req.GET['lastname']

    sql = """insert into userProfile (firstname, lastname, num_employee) values (%s, %s, %s)"""
    val = (fname, lname, 12346)
    cursor.execute(sql, val)
    connection.commit()

    html_content = "<html><head><title>Hello</title></head><body>"
    html_content += "<strong>" + fname + ", Data record has been stored in the Database</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"

    return HttpResponse(html_content)