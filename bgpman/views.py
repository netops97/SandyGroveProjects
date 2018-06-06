from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Router
from .forms import RouterForm
from pages.models import Page
import time
import paramiko
import re

@login_required(login_url=reverse_lazy('login'))
def router_req(request):
    print('View: router_req')
    ts = time.time()
    print('Timestamp: ', ts)
    submitted = False
    session_failure = False
    if request.method == 'POST':
        print('View: POST method')
        form = RouterForm(request.POST)
        if form.is_valid():
            ipaddr = form.cleaned_data['address']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            state = form.cleaned_data['state']
            print('View: ipaddr=', ipaddr)
            print('View: username=', username)
            print('View: password=', password)
            print('View: state=',state)
            #form.save()
            if session_manager(ipaddr,username,password,state):
                print("View: Save to DB")
                print("View: Redirect")
                form.save()
                return HttpResponseRedirect('/bgpman?submitted=True')
            else:
                print("View: Redirect")
                return HttpResponseRedirect('/bgpman?session_failure=True')

        else:
            print("View: form NOT valid")
    else:
        form = RouterForm()
        print('View: GET method')
        if 'submitted' in request.GET:
            submitted = True
        if 'session_failure' in request.GET:
            session_failure = True

    #assert False
    print('View: submitted = ',submitted)
    print('View: session_failure = ',session_failure)
    print('View: render')
    return render(request, 'bgpman/bgpman.html',
     {'form': form,
      'page_list': Page.objects.all(),
      'submitted': submitted,
      'session_failure': session_failure})

# BGP session manager logs into the target router and based on arguments,
# issues a shut or no shut command to the BGP session
def session_manager (ipaddr, username, password, state):

    port = 22
    ssh=paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ipaddr, port, username, password)

    except Exception:
        ssh.close()
        print("Session: SSH authentication failed!")
        return False;
    else:
        print("Session: SSH authentication passed!")



    # Shell sessions are used versus Individual commands
    remote_conn = ssh.invoke_shell()
    output = remote_conn.recv(65535)
    #print (output)

    remote_conn.send("show bgp sum\n")
    time.sleep(.5)
    s = remote_conn.recv(65535)
    output = s.decode('utf-8')
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output )
    print("Session: Neighbor IP: ", ip[2])
    #print (output)

    remote_conn.send("conf t\n")
    time.sleep(.5)
    output = remote_conn.recv(65535)
    print("Session: Configure Terminal")
    #print (output)

    remote_conn.send("router bgp 65535\n")
    time.sleep(.5)
    output = remote_conn.recv(65535)
    print("Session: router BGP 65535")
    #print (output)

    # what about single router sites???
    session_cmd = "neighbor " + ip[2] + " shutdown\n"

    searchObj = re.search(r'ISOLATE',state , re.M|re.I )
    if searchObj:
        remote_conn.send(session_cmd)
        time.sleep(.5)
        output = remote_conn.recv(65535)
        #stripping line feed control character from command string
        #for debug display
        session_cmd = "neighbor " + ip[2] + " shutdown"
        print("Session:", session_cmd)
        #print (output)

    session_cmd = "no neighbor " + ip[2] + " shutdown\n"

    searchObj = re.search(r'NORM',state , re.M|re.I )
    if searchObj:
        remote_conn.send(session_cmd)
        time.sleep(.5)
        output = remote_conn.recv(65535)
        #stripping line feed control character from command string
        #for debug display
        session_cmd = "no neighbor " + ip[2] + " shutdown"
        print("Session:", session_cmd)
        #print (output)

    remote_conn.send("end\n")
    time.sleep(.5)
    output = remote_conn.recv(65535)
    #print (output)

    ssh.close()
    return True;
