import httplib
import json
import re
import requests
import thread
import daemon

# conn = httplib.HTTPSConnection("http://0.0.0.0:5100")
base = "/api/v1/2af0482f74dc27040b81bcbd0d69bfe85381c9026b0edaa194a0c2a69e1f0c9f"
headers = {"Accept": "application/json"}

def user_status(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/user/status"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_home(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/user/home"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_search(app_token="", user_name=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/user/search/%s"%(base, app_token, user_name))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_app_connectivity(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/connectivity"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

# Messages
def user_message_create(app_token="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/message/create"%(base, app_token), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_message_show(app_token="", message_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/message/show/%s"%(base, app_token, message_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_message_update(app_token="", message_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/message/update/%s"%(base, app_token,message_id), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_message_delete(app_token="", message_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/message/delete/%s"%(base, app_token, message_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_get_messages(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/messages"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

# Files
def user_file_create(app_token="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/file/create"%(base, app_token), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_file_show(app_token="", file_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/file/show/%s"%(base, app_token, file_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_file_update(app_token="", file_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/file/update/%s"%(base, app_token,file_id), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_file_delete(app_token="", file_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/file/delete/%s"%(base, app_token, file_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_file_upload(app_token="", group='unknown', item_id="", file_name=""):
    url = "http://0.0.0.0:5100%s/%s/file/upload/%s/%s"%(base, app_token,group,item_id)
    files = {'file': open('%s'%file_name)}
    response = requests.post(url, files=files)
    return response.content

def user_file_download(app_token="", file_id=""):
    url = "http://0.0.0.0:5100%s/%s/file/download/%s"%(base, app_token, file_id)
    # conn = httplib.HTTPConnection("0.0.0.0", 5100)
    # conn.request("GET","%s/%s/file/download/%s"%(base, app_token, file_id))
    # response = conn.getresponse()
    response = requests.get(url)
    # return "Headers: %s"%response.headers
    content = response.content
    d = response.headers['Content-Disposition']
    fname = re.findall("filename=(.+)", d)
    with open(fname[0], 'w') as downloaded_f:
        downloaded_f.write(content)
    return '%s Downloaded'%fname

def user_get_files(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/files"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

# Projects
def user_project_create(app_token="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST", "%s/%s/project/create"%(base, app_token), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_project_show(app_token="", project_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/project/show/%s"%(base, app_token, project_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_project_delete(app_token="", project_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/project/delete/%s"%(base, app_token, project_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_get_projects(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/projects"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data


# +++ Records

def user_record_create(app_token="", project_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST", "%s/%s/project/record/create/%s"%(base, app_token, project_id), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_record_show(app_token="", record_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/record/show/%s"%(base, app_token, record_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_record_update(app_token="", record_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST", "%s/%s/record/update/%s"%(base, app_token, record_id), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_record_delete(app_token="", record_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/record/delete/%s"%(base, app_token, record_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_get_records(app_token="", project_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/project/records/list/%s"%(base, app_token, project_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_download_record(app_token="", record_id=""):
    url = "http://0.0.0.0:5100%s/%s/record/download/%s"%(base, app_token, record_id)
    response = requests.get(url)
    content = response.content
    d = response.headers['Content-Disposition']
    fname = re.findall("filename=(.+)", d)
    with open(fname[0], 'w') as downloaded_f:
        downloaded_f.write(content)
    return '%s Downloaded'%fname

# --- Diff

def user_diff_create(app_token="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/diff/create"%(base, app_token), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_diff_show(app_token="", diff_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/diff/show/%s"%(base, app_token, diff_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_diff_update(app_token="", diff_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/diff/update/%s"%(base, app_token,diff_id), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_get_diffs(app_token=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/diffs"%(base, app_token))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

# --- Env

def user_update_env_bundle(app_token="", bundle="", file_name=""):
    def handle_file_resolution(bundle, file_name):
        url = "http://0.0.0.0:5100%s/%s/file/upload/bundle/%s"%(base, app_token, bundle)
        files = {'file': open('%s'%file_name)}
        response = requests.post(url, files=files)
        print response.content
        with open('user-bundle-%s-upload.log'%bundle, 'w') as bundle_log:
            bundle_log.write(response.content)

    # handle_file_resolution(bundle, file_name)
    with daemon.DaemonContext():
        handle_file_resolution(bundle, file_name)
    # thread.start_new_thread(handle_file_resolution, (bundle, file_name,))
    # t = threading.Thread(target = handle_file_resolution, args=(bundle, file_name,)).start()    
    return 'Thread sheduled for upload!'

def user_project_env_next(app_token="", project_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/project/env/next/%s"%(base, app_token, project_id), json.dumps(data), headers)
    response = conn.getresponse()
    print response.status
    data = response.read()
    conn.close()
    return data

def user_project_env_update(app_token="", project_id="", env_id="", data={}):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("POST","%s/%s/project/env/update/%s/%s"%(base, app_token, project_id, env_id), json.dumps(data), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_project_envs(app_token="", project_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/project/envs/%s"%(base, app_token, project_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_project_envs_head(app_token="", project_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/project/envs/head/%s"%(base, app_token, project_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def user_project_env_show(app_token="", project_id="", env_id=""):
    conn = httplib.HTTPConnection("0.0.0.0", 5100)
    conn.request("GET","%s/%s/project/env/show/%s/%s"%(base, app_token, project_id, env_id))
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

if __name__ == '__main__':

    print user_status('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    print user_home('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    # print user_search('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', 'User2-CoRR')
    # print user_search('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', 'CoRR')

    print user_app_connectivity('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    
    message1 = {
        "receiver":"56731c3a9f9d5110105a27f4",
        "title":"Test New Message 1",
        "content":"This is a test from user api."
    }

    message2 = {
        "receiver":"56731c3a9f9d5110105a27f4",
        "title":"Test New Message 2",
        "content":"This is another test from user api."
    }

    message3 = {
        "receiver":"56731c3a9f9d5110105a27f4",
        "title":"Test New Message 3",
        "content":"This is yet another test from user api."
    }

    # print user_get_messages('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    # print user_message_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', message1)
    # print user_message_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', message2)
    # print user_message_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', message3)
    # print user_get_messages('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    # print user_message_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f8')
    # message3['content'] = 'This is yet another updated message done from the user api.'
    # print user_message_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f8', message3)
    # print user_message_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f8')
    # print user_message_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f7')
    # print user_message_delete('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f7')
    # print user_message_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f7')


    file1 = {
        "name":"Another reference to pymks-paper-2015.pdf",
        "storage":"566b18159f9d516b595d7e19_pymks-paper-2015.pdf",
        "group": "resource",
        "description":"This a resource pdf file of a PyMKS paper."
    }

    file2 = {
        "name":"An Introduction to Quantum Computing",
        "storage":"http://sergeev.fiz.univ.szczecin.pl/Dydaktyka/Wyklady/Kaye.pdf",
        "group": "file",
        "access": "private",
        "description":"We have offered a course at the University of Waterloo in quantum comput-\
                       ing since 1999. We have had students from a variety of backgrounds take the\
                       course, including students in mathematics, computer science, physics, and engi-\
                       neering. While there is an abundance of very good introductory papers, surveys\
                       and books, many of these are geared towards students already having a strong\
                       background in a particular area of physics or mathematics."
    }

    # print user_get_files('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    # print user_file_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '56747b939f9d51373dc0a5ec')
    # print user_file_download('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '56747b939f9d51373dc0a5ec')
    # print user_file_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', file1)
    # print user_file_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', file2)
    # print user_get_files('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')

    # print user_file_upload('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', 'attach-message', '567b106b9f9d517f31ec24f8', '0602096.pdf')
    # print user_get_files('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    # # Show the uploaded file and download it.
    # print user_file_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '56731cbd9f9d5110105a27fa')
    # print user_file_download('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '56731cbd9f9d5110105a27fa')

    #File 2 download
    # print user_file_download('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f8')

    # file1['description'] = 'This is an updated description of the PyMKS paper.'
    # print user_file_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f8', file1)
    # print user_file_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f8')

    # # File 1 delete
    # print user_file_delete('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f7')
    # print user_file_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567b106b9f9d517f31ec24f7')

    
    project1 = {
        "name":"Python-Qrcode",
        "description":"This module uses image libraries, Python Imaging Library (PIL) by default, to generate QR Codes. It is recommended to use the pillow fork rather than PIL itself.",
        "goals":"A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)",
        "tags":["code","unique","pictographic"],
        "group":"computational"
    }
    project2 = {
        "name":"Muon Detector Simulation",
        "description":"This program allows the user to simulate a Muon Detector with a specified number of Muons at a specified starting energy in MeV.",
        "goals":"To get the program to work the user needs to change the path for which they want the two, final, comma seperated value file to save to this can be located in the 'Histogram' class under the method 'writeToDisk'. If the user does not specify the file path before running the program then it will not save the data for simulated muon paths. The data can be observed in Microsoft Excel by plotting the x-postion or Bin value against both energy and y-value depending on which comma seperated value file was opened. The user can also add aditional detector materials and create instances to do this. The detector is currently made from Iron this is a dense material that Muons will interact with.",
        "tags":["simulation","muon","tomography"],
        "group":"computational"
    }

    # print user_get_projects('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')
    # print user_project_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', project1)
    # print user_project_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', project2)
    # print user_get_projects('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')


    env1 = {
        "group":"computational",
        "system":"container-based",
        "specifics":{'container-system':'docker', 'container-version':'1.0'},
        "version":{
            "system":"git",
            "baseline":"develop",
            "marker":"9c264611cf9af99057ac31d3f863fa300da8e2d7"
        },
        "bundle":{
            "location":"https://s3-us-west-2.amazonaws.com/ddsm-bucket/5595f1b789adcc1556eb41cd-5597914cc922f075f076fa35-unknown.tar"
        }
    }
    env2 = {
        "group":"computational",
        "system":"container-based",
        "specifics":{'container-system':'docker', 'container-version':'1.0'},
        "version":{
            "system":"git",
            "baseline":"master",
            "marker":"35d3d3de724af4dec758be1c02fb56f0600b16b8"
        },
        "bundle":{
            "location":"https://s3-us-west-2.amazonaws.com/ddsm-bucket/5595f1b789adcc1556eb41cd-559aa346c922f009dbc3b872-unknown.tar"
        }
    }

    env3 = {
        "group":"computational",
        "system":"container-based",
        "specifics":{'container-system':'docker', 'container-version':'1.0'},
        "version":{
            "system":"git",
            "baseline":"master",
            "marker":"35d3d3de724af4dec758be1c02fb56f0600b1634"
        },
        "bundle":{
            "location":"https://s3-us-west-2.amazonaws.com/ddsm-bucket/5595f1b789adcc1556eb41cd-559aa346c922f009dbc3b872-unknown.tar"
        }
    }

    print user_project_envs_head('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8')
    print user_project_envs_head('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c')
    print user_project_envs_head('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029')
    
    # print user_project_envs('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8')
    # print user_project_envs('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c')

    # print user_project_env_next('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8', env1)
    # print user_project_env_next('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', env2)
    # print user_project_env_next('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029', env3)

    # print user_project_envs_head('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8')
    # print user_project_envs_head('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c')

    # print user_project_envs('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8')
    # print user_project_envs('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c')

    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8', '5684068b9f9d5134b5e01335')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '56747b939f9d51373dc0a5ea')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '5684068b9f9d5134b5e01338')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029', '56840b129f9d5137d5675488')
    
    # !!!Second parameter is the bundle id.
    # print user_update_env_bundle('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '5684068b9f9d5134b5e01337', '/home/fyc/Documents/Projects/NIST/CoRR/github/demo-sumatra.tar')
    # print user_update_env_bundle('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '56840b129f9d5137d567548a', '/home/fyc/Documents/Projects/NIST/CoRR/github/presentation_11-23-2015.pdf')
    # print user_update_env_bundle('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '56747b939f9d51373dc0a5ec', '/home/fyc/Documents/Projects/NIST/CoRR/github/Howe_chapter.pdf')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8', '5684068b9f9d5134b5e01335')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '56747b939f9d51373dc0a5ea')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '5684068b9f9d5134b5e01338')
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029', '56840b129f9d5137d5675488')
    # env2['bundle']['location'] = "https://s3-us-west-2.amazonaws.com/ddsm-bucket/5595f1b789adcc1556eb41cd-5597914cc922f075f076fa35-unknown.tar"
    # print user_project_env_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '5684068b9f9d5134b5e01338', env2)
    # print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '5684068b9f9d5134b5e01338')

    print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8', '5684068b9f9d5134b5e01335')
    print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '56747b939f9d51373dc0a5ea')
    print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c', '5684068b9f9d5134b5e01338')
    print user_project_env_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029', '56840b129f9d5137d5675488')


    # Records

    record1 = {
        "project":"568405659f9d51159513e6a8",
        "system":{
            "architecture_bits": "64bit",
            "architecture_linkage": "ELF",
            "ip_addr": "127.0.0.1",
            "machine": "x86_64",
            "network_name": "606d8d28528d",
            "processor": "Intel Core i7-4470HQ CPU @ 2.20Ghz x 8",
            "gpu":"Intel Iris Pro Graphics 5200 (GT3 + 128 MB eDRAM)",
            "release": "3.19.0-18-generic",
            "system_name": "Linux",
            "distribution": "Ubuntu 15.04",
            "version": "#18-Ubuntu SMP Tue May 19 18:31:35 UTC 2015"
        },
        "inputs":[
            {
                "parameters": {

                    "content": "modulus = 100, 120 # Elastic modulus\nratio = 0.3, 0.3 # Poissons ratio\nstrain = 0.02 # Macro strain\nsize = 21, 21 # Microstructure size",
                    "type": "SimpleParameterSet"
                }
            },
            {
                "script_arguments": "<parameters>"
            }
        ],
        "outputs":[
            {
                "creation": "2015-07-01 04:53:59",
                "digest": "43a47cb379df2a7008fdeb38c6172278d000fdc4",
                "metadata": {
                    "encoding": '',
                    "mimetype": '',
                    "size": 2500
                },
                "path": "example2.dat"
            }
        ],
        "dependencies":[
            {
                "diff": "",
                "module": "python",
                "name": "_markerlib",
                "path": "/usr/lib/python2.7/dist-packages/_markerlib",
                "source": '',
                "version": "unknown"
            },
            {
                "diff": "",
                "module": "python",
                "name": "numpy",
                "path": "/usr/lib/python2.7/dist-packages/numpy",
                "source": "attribute",
                "version": "1.8.2"
            },
            {
                "diff": "",
                "module": "python",
                "name": "pymks",
                "path": "/usr/lib/python2.7/dist-packages/pymks",
                "source": "attribute",
                "version": "0.2.3"
            },
            {
                "diff": "",
                "module": "python",
                "name": "setuptools",
                "path": "/usr/lib/python2.7/dist-packages/setuptools",
                "source": "attribute",
                "version": "3.3"
            }
        ],
        "status":"running",
        "rationels":[
            "Compute the linear strain field for a two phase composite material",
            "Linear Elasticity in 2D"
        ]
    }

    record2 = {
        "project":"567321a49f9d511391055d1c",
        "system":{
            "architecture_bits": "64bit",
            "architecture_linkage": "ELF",
            "ip_addr": "127.0.0.1",
            "machine": "x86_64",
            "network_name": "606d8d28528d",
            "processor": "Intel Core i7-4470HQ CPU @ 2.20Ghz x 8",
            "gpu":"Intel Iris Pro Graphics 5200 (GT3 + 128 MB eDRAM)",
            "release": "3.19.0-18-generic",
            "system_name": "Linux",
            "distribution": "Ubuntu 15.04",
            "version": "#18-Ubuntu SMP Tue May 19 18:31:35 UTC 2015"
        },
        "inputs":[
            {
                "script_arguments": "<parameters>"
            }
        ],
        "outputs":[
            {
                    "stdout_stderr": "Not launched."
            },
            {
                "stdout_stderr": "No output."
            }
        ],
        "dependencies":[
            {
                "diff": "",
                "module": "python",
                "name": "_markerlib",
                "path": "/usr/lib/python2.7/dist-packages/_markerlib",
                "source": '',
                "version": "unknown"
            },
            {
                "diff": "",
                "module": "python",
                "name": "numpy",
                "path": "/usr/lib/python2.7/dist-packages/numpy",
                "source": "attribute",
                "version": "1.8.2"
            },
            {
                "diff": "",
                "module": "python",
                "name": "fipy",
                "path": "/usr/lib/python2.7/dist-packages/fipy",
                "source": "attribute",
                "version": "3.1"
            },
            {
                "diff": "",
                "module": "python",
                "name": "setuptools",
                "path": "/usr/lib/python2.7/dist-packages/setuptools",
                "source": "attribute",
                "version": "3.3"
            }
        ],
        "status":"starting",
        "rationels":[
            "First record",
            "Simple example for integration",
            "Crank-Nicholson transient diffusion"
        ]
    }

    record3 = {
        "project":"568409159f9d5136e4351029",
        "system":{
            "architecture_bits": "64bit",
            "architecture_linkage": "ELF",
            "ip_addr": "127.0.0.1",
            "machine": "x86_64",
            "network_name": "606d8d28528d",
            "processor": "Intel Core i7-4470HQ CPU @ 2.20Ghz x 8",
            "gpu":"Intel Iris Pro Graphics 5200 (GT3 + 128 MB eDRAM)",
            "release": "3.19.0-18-generic",
            "system_name": "Linux",
            "distribution": "Ubuntu 15.04",
            "version": "#18-Ubuntu SMP Tue May 19 18:31:35 UTC 2015"
        },
        "inputs":[
            {
                "script_arguments": "<parameters>"
            }
        ],
        "outputs":[
            {
                    "stdout_stderr": "Not launched."
            },
            {
                "stdout_stderr": "No output."
            }
        ],
        "dependencies":[
            {
                "diff": "",
                "module": "python",
                "name": "_markerlib",
                "path": "/usr/lib/python2.7/dist-packages/_markerlib",
                "source": '',
                "version": "unknown"
            },
            {
                "diff": "",
                "module": "python",
                "name": "numpy",
                "path": "/usr/lib/python2.7/dist-packages/numpy",
                "source": "attribute",
                "version": "1.8.2"
            },
            {
                "diff": "",
                "module": "python",
                "name": "fipy",
                "path": "/usr/lib/python2.7/dist-packages/scikitlearn",
                "source": "attribute",
                "version": "2.9"
            },
            {
                "diff": "",
                "module": "python",
                "name": "setuptools",
                "path": "/usr/lib/python2.7/dist-packages/setuptools",
                "source": "attribute",
                "version": "3.3"
            }
        ],
        "status":"starting",
        "rationels":[
            "Test record",
            "Machine learning test"
        ]
    }

    print user_get_records('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8')
    print user_get_records('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c')
    print user_get_records('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029')

    # print user_record_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8', record1)
    # print user_record_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029', record2)
    # print user_record_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029', record3)

    # print user_get_records('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568405659f9d51159513e6a8')
    # print user_get_records('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567321a49f9d511391055d1c')
    # print user_get_records('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568409159f9d5136e4351029')

    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b33')
    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567322d09f9d5113c3a63dea')
    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b36')
    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b38')

    # print user_record_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b33', {'access':'public'})
    # print user_record_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567322d09f9d5113c3a63dea', {'access':'private'})
    # print user_record_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b36', {'access':'public'})
    # print user_record_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b38', {'access':'public'})

    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b33')
    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '567322d09f9d5113c3a63dea')
    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b36')
    # print user_record_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b38')

    print user_download_record('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '568550149f9d513065c68b33')

    # ++ Diff
    diff1 = {
        "from":"568550149f9d513065c68b36",
        "to":"568550149f9d513065c68b38",
        "method":"default",
        "proposition":"reproduced",
        "status":"proposed"
    }

    diff2 = {
        "from":"568550149f9d513065c68b36",
        "to":"568550149f9d513065c68b33",
        "method":"visual",
        "proposition":"reproduced",
        "status":"proposed"
    }

    # print user_get_diffs('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')

    # print user_diff_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', diff1)
    # print user_diff_create('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', diff2)

    # print user_get_diffs('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a')

    # print user_diff_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '5685596a9f9d514743604331')
    # print user_diff_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '5685596a9f9d514743604332')

    # diff2['status'] = 'agreed'

    # print user_diff_update('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '5685596a9f9d514743604332', diff2)

    # print user_diff_show('dad86479d3f0e4b1c6ed17b8ab02a9df4fa65e61761d5952f45770c19fb5194a', '5685596a9f9d514743604332')


























