#Summary: This utility access skydrive, and use REST api to upload files. 
#Author: Jiangong Li
#Email: jgli_2008@sina.com

from http import cookiejar
import urllib.request, urllib.parse, urllib.error

import json

class From:
	def __Init__(self):
		self.name = ""
		self.id = ""

class Shared_with:
	def __init__(self):
		self.access = "Everyone (public)"


class File:
	def __init__(self):
		self.id = ""
		self.from_info = From()
		self.name = ""
		self.description = ""
		self.parent_id = ""
		self.size = 0
		self.upload_location = ""
		self.comments_count = 0
		self.comments_enabled = True
		self.is_embeddable = True
		self.source = ""
		self.link = ""
		self.type = "file"
		self.shared_with = Shared_with()
		self.created_time = ""
		self.updated_time = ""
		self.sort_by = "updated"


class SkyDrive:
	#moduleUrl: /me/skydrive/files
	def __init__(self, moduleUrl = '/me/skydrive/files'):
		self.access_token = ""
		self.module_url = moduleUrl
		self.scope = 'wl.basic wl.skydrive_update wl.offline_access'
		self.apiServer = 'https://apis.live.net/v5.0/'
		self.clientid = '00000000440FB8ED'
		self.clientSecret = 'lFEPMixjcMddTKpSMCbR6NqxHe8n-FdL'
		self.authorizeServer = 'https://login.live.com/oauth20_authorize.srf'
		self.oauthServer = 'https://login.live.com/oauth20_token.srf'
		self.redirectUri = 'https://login.live.com/oauth20_desktop.srf'
		
		pass

	def authorizeUri(self):
		url = self.authorizeServer + "?"
		url += 'client_id=' + self.clientid + '&'
		url += 'scope=' + urllib.parse.quote(self.scope) + '&'
		url += 'response_type=code'
		url += '&'
		url += "redirect_uri=" + ''#self.redirectUri

		return url

	def accessUri(self):
		return '%s%s?access_token=%s'%(self.apiServer, self.module_url, self.access_token)

	def login(self):
		data = {}

		data['client_id'] = self.clientid
		data['client_secret'] = self.clientSecret
		data['redirect_uri'] = self.redirectUri
		data['refresh_token'] = 'tGzv3JOkF0XG5Qx2TlKWIA'
		data['grant_type'] = 'refresh_token'
		
		url = self.oauthServer	

	    #open access url
		#resp = urllib.request.urlopen(url, urllib.parse.urlencode(data).encode('utf-8'))
		resp = urllib.request.urlopen(self.authorizeUri())
		print(resp.info())
		print(resp.status)

	def upload(self, data):
		header_boundary = 'A333x'
		header_content_type = 'multipart/form-data; boundary=%s'%(header_boundary)
		sub_content_disposition = 'form-data; name=\"%(name)s\"; filename=\"%(filename)s\"'
		sub_content_type = 'application/octet-stream'

		#build request data
		postdata = "--" + header_boundary + "\r\n"
		postdata += "Content-Disposition: " + sub_content_disposition + "\r\n"
		postdata ++ "Content-Type:" + sub_content_type + "\r\n"

		posdata += "--" + header_boundary + "--"

		#build request for accessed url
		homeReq = urllib.request.Request(
			url = self.url,
			data = data.encode('utf-8')
			)

		homeReq.add_header('Content-Type', header_content_type)


		#open access url
		resp = urllib.request.urlopen(homeReq)
		print(resp.info())
		print(resp.status)

		pass



def main():
	skydrive = SkyDrive()
	skydrive.login()

	pass

if __name__ == '__main__':
	main()