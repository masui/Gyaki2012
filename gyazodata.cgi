#!/opt/local/bin/ruby -rubygems
# -*- coding: utf-8-emacs -*-
# -*- ruby -*-
#
# Canvasに画像を読み込んで編集しようとするとクロスドメインエラーになるので
# Gyaki上のこのCGIを中継することにする
# http://shokai.org/blog/archives/5668
#

require 'cgi'
require 'net/http'

cgi = CGI.new("html3")

id = cgi.params['id'][0].to_s

gyazo_host = 'gyazo.com'
gyazo_ua   = 'Gyazo/1.0'

res = Net::HTTP.start(gyazo_host,80){|http|
  http.get("/"+id+".png");
}

data = res.read_body

cgi.out { data }


