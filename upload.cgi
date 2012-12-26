#!/opt/local/bin/ruby -rubygems
# -*- coding: utf-8-emacs -*-
# -*- ruby -*-
#
# AndroGyazoからのリクエストに応じて画像データをGyazoにアップロード
#
require 'cgi'
require 'base64'
require 'net/http'

cgi = CGI.new("html3")

id = cgi.params['id'][0].to_s
data = cgi.params['data'][0].to_s

data.sub!(/^.*base64,/,'')
imagedata = Base64.decode64(data)

boundary = '----BOUNDARYBOUNDARY----'
gyazo_host = 'gyazo.com'
gyazo_cgi = '/upload.cgi'
gyazo_ua   = 'Gyazo/1.0'
data = <<EOF
--#{boundary}\r
content-disposition: form-data; name="id"\r
\r
#{id}\r
--#{boundary}\r
content-disposition: form-data; name="imagedata"; filename="gyazo.com"\r
\r
#{imagedata}\r
--#{boundary}--\r
EOF
header ={
  'Content-Length' => data.length.to_s,
  'Content-type' => "multipart/form-data; boundary=#{boundary}",
  'User-Agent' => gyazo_ua
}
res = Net::HTTP.start(gyazo_host,80){|http|
  http.post(gyazo_cgi,data,header)
}

url = res.read_body

cgi.out { url }


