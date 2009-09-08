#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2009, Walter Bender

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import sys
import os
import os.path
import gettext

def main():

    myname = "turtlegroup"
    if len(sys.argv) != 2:
        print "Error: Usage is " + myname + ".py lang"
        return

    t = gettext.translation("org.laptop.TurtleArtActivity", "../locale", \
                            languages=[sys.argv[1]])
    _ = t.ugettext
    t.install()

    mystring1 = _("clean")
    mystring2 = _("forward")
    mystring3 = _("back")
    mystring4 = _("left")
    mystring5 = _("right")
    mystring6 = _("arc")
    mystring7 = _("angle")
    mystring8 = _("radius")
    mystring9 = _("setyx")
    mystring10 = _("x")
    mystring11 = _("y")
    mystring12 = _("set heading")
    mystring13 = _("xcor")
    mystring14 = _("ycor")
    mystring15 = _("heading")
    mystring16 = _("Turtle")
    mystring17 = _("show")
    mystring18 = _("set scale")
    mystring19 = _("name")
    mygroup = "turtle"

    print mystring1
    print mystring2
    print mystring3
    print mystring4
    print mystring5
    print mystring6
    print mystring7
    print mystring8
    print mystring9
    print mystring10
    print mystring11
    print mystring12
    print mystring13
    print mystring14
    print mystring15
    print mystring16
    print mystring17
    print mystring18
    print mystring19

    data0 = \
"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\
<!-- Created with Inkscape (http://www.inkscape.org/) -->\
<svg\
   xmlns:svg=\"http://www.w3.org/2000/svg\"\
   xmlns=\"http://www.w3.org/2000/svg\"\
   xmlns:xlink=\"http://www.w3.org/1999/xlink\"\
   version=\"1.0\"\
   width=\"145\"\
   height=\"500\"\
   id=\"svg2\">\
  <defs\
     id=\"defs103\">\
    <linearGradient\
       id=\"linearGradient3250\">\
      <stop\
         id=\"stop3252\"\
         style=\"stop-color:#ffffff;stop-opacity:1\"\
         offset=\"0\" />\
      <stop\
         id=\"stop3254\"\
         style=\"stop-color:#00ff00;stop-opacity:1\"\
         offset=\"1\" />\
    </linearGradient>\
    <linearGradient\
       x1=\"0\"\
       y1=\"22\"\
       x2=\"74\"\
       y2=\"22\"\
       id=\"linearGradient3256\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"22\"\
       x2=\"74\"\
       y2=\"22\"\
       id=\"linearGradient3258\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"22\"\
       x2=\"74\"\
       y2=\"22\"\
       id=\"linearGradient3260\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"22\"\
       x2=\"74\"\
       y2=\"22\"\
       id=\"linearGradient3264\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"22\"\
       x2=\"74\"\
       y2=\"22\"\
       id=\"linearGradient3267\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"7\"\
       y1=\"90\"\
       x2=\"56\"\
       y2=\"90\"\
       id=\"linearGradient3333\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"7\"\
       y1=\"130\"\
       x2=\"56\"\
       y2=\"130\"\
       id=\"linearGradient3341\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"90\"\
       x2=\"128\"\
       y2=\"90\"\
       id=\"linearGradient3349\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"130\"\
       x2=\"128\"\
       y2=\"130\"\
       id=\"linearGradient3357\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"43\"\
       y1=\"181\"\
       x2=\"92\"\
       y2=\"181\"\
       id=\"linearGradient3365\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"7\"\
       y1=\"251\"\
       x2=\"56\"\
       y2=\"251\"\
       id=\"linearGradient3373\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3381\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"6\"\
       y1=\"303\"\
       x2=\"72\"\
       y2=\"303\"\
       id=\"linearGradient3389\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"89\"\
       y1=\"314\"\
       x2=\"137\"\
       y2=\"314\"\
       id=\"linearGradient3397\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"37\"\
       y1=\"359\"\
       x2=\"107\"\
       y2=\"359\"\
       id=\"linearGradient3405\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(0,26)\" />\
    <linearGradient\
       x1=\"37\"\
       y1=\"382\"\
       x2=\"107\"\
       y2=\"382\"\
       id=\"linearGradient3413\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(0,26)\" />\
    <linearGradient\
       x1=\"37\"\
       y1=\"406\"\
       x2=\"107\"\
       y2=\"406\"\
       id=\"linearGradient3421\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(0,26)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient2505\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient2519\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"37\"\
       y1=\"406\"\
       x2=\"107\"\
       y2=\"406\"\
       id=\"linearGradient2527\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"0\"\
       x2=\"100\"\
       y2=\"66\"\
       id=\"linearGradient3172\"\
       xlink:href=\"#linearGradient3166\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       id=\"linearGradient3166\">\
      <stop\
         id=\"stop3168\"\
         style=\"stop-color:#ffffff;stop-opacity:1\"\
         offset=\"0\" />\
      <stop\
         id=\"stop3170\"\
         style=\"stop-color:#00ff00;stop-opacity:1\"\
         offset=\"1\" />\
    </linearGradient>\
    <linearGradient\
       x1=\"0\"\
       y1=\"0\"\
       x2=\"100\"\
       y2=\"20\"\
       id=\"linearGradient2707\"\
       xlink:href=\"#linearGradient3166\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"matrix(0.7,0,0,1.,0.1,32)\" />\
    <linearGradient\
       id=\"linearGradient2701\">\
      <stop\
         id=\"stop2703\"\
         style=\"stop-color:#ffffff;stop-opacity:1\"\
         offset=\"0\" />\
      <stop\
         id=\"stop2705\"\
         style=\"stop-color:#ffff00;stop-opacity:1\"\
         offset=\"1\" />\
    </linearGradient>\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient2732\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"0\"\
       x2=\"100\"\
       y2=\"66\"\
       id=\"linearGradient2736\"\
       xlink:href=\"#linearGradient3166\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"matrix(0.67,0,0,0.67,60,321)\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"0\"\
       x2=\"100\"\
       y2=\"66\"\
       id=\"linearGradient3552\"\
       xlink:href=\"#linearGradient3166\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"matrix(0.67,0,0,0.67,60,321)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3554\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\" />\
    <linearGradient\
       x1=\"37\"\
       y1=\"359\"\
       x2=\"107\"\
       y2=\"359\"\
       id=\"linearGradient2696\"\
       xlink:href=\"#linearGradient2701\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(26.1,-84.4)\" />\
    <linearGradient\
       x1=\"0\"\
       y1=\"0\"\
       x2=\"100\"\
       y2=\"66\"\
       id=\"linearGradient2711\"\
       xlink:href=\"#linearGradient2701\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"matrix(0.67,0,0,0.67,63.4,348)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3486\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(-65.6,64.2)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3495\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(-66.6,99)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3502\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(-65.5,133)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3533\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(-66.6,99)\" />\
    <linearGradient\
       x1=\"79\"\
       y1=\"238\"\
       x2=\"128\"\
       y2=\"238\"\
       id=\"linearGradient3535\"\
       xlink:href=\"#linearGradient3250\"\
       gradientUnits=\"userSpaceOnUse\"\
       gradientTransform=\"translate(-65.6,64.2)\" />\
  </defs>\
  <path\
     d=\"M 0.58809792,0.55108212 L 0.52581012,484.98977 L 3.6485499,492.43821 L 8.520663,496.82385 L 15.179825,499.47419 L 128.96395,499.47419 L 135.80997,496.63739 L 141.75709,491.22606 L 144.47996,482.0929 L 144.51764,0.52581012 L 0.58809792,0.55108212 z\"\
     id=\"path30\"\
     style=\"fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137\"\
     height=\"0\"\
     x=\"3.7\"\
     y=\"213\"\
     id=\"rect32\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"214.3\"\
     id=\"rect34\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"215\"\
     id=\"rect36\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#ffffc4;stroke-width:1;stroke-opacity:1\" />\
  <g\
     id=\"g2681\">\
    <rect\
       width=\"138.11\"\
       height=\"0.11000219\"\
       x=\"3.4449987\"\
       y=\"65.445\"\
       id=\"rect38\"\
       style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:0.88999784;stroke-opacity:1\" />\
    <rect\
       width=\"137.5\"\
       height=\"0.14\"\
       x=\"3.5\"\
       y=\"66.360001\"\
       id=\"rect40\"\
       style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" />\
    <rect\
       width=\"138.11032\"\
       height=\"0.11032366\"\
       x=\"3.444838\"\
       y=\"67.444839\"\
       id=\"rect42\"\
       style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#ffffc4;stroke-width:0.88967633;stroke-opacity:1\" />\
  </g>\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"-26.9\"\
     transform=\"scale(1,-1)\"\
     id=\"rect44\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"-25.799999\"\
     transform=\"scale(1,-1)\"\
     id=\"rect46\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"-472.70001\"\
     transform=\"scale(1,-1)\"\
     id=\"rect48\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"-471.39999\"\
     transform=\"scale(1,-1)\"\
     id=\"rect50\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 134,491 C 134,492 133,493 132,493 C 131,493 131,492 131,491 C 131,491 131,490 132,490 C 133,490 134,491 134,491 z\"\
     id=\"path58\"\
     style=\"fill:#fff080;fill-opacity:1;stroke:none;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 80,485 C 80,490 77,493 72,493 C 67,493 64,490 64,485 C 64,481 67,477 72,477 C 77,477 80,481 80,485 L 80,485 z\"\
     id=\"path60\"\
     style=\"fill:#ff4040;fill-opacity:1;stroke:#ff4040;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text54\"\
     style=\"font-size:12px;font-weight:bold;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"68\"\
       y=\"489\"\
       id=\"tspan56\"\
       style=\"font-size:12px;font-weight:bold;fill:#ffffff;font-family:Bitstream Vera Sans\">X</tspan>\
  </text>\
  <path\
     d=\"M 79,32 C 90,32 90,32 90,32 L 94,35 L 96,39 L 96,52 L 94,55 L 90,58 L 79,58 L 79,58 L 79,60 L 65,60 L 65,58 L 54,58 L 50,55 L 48,52 L 48,39 L 50,35 L 54,32 L 65,32 L 65,36 L 79,36 L 79,32 z\"\
     id=\"path59\"\
     style=\"fill:url(#linearGradient3267);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text61\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;fill:#000000;fill-opacity:1;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"72\"\
       y=\"49\"\
       id=\"tspan63\"\
       style=\"font-size:12px\">"

    data1 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 54,77 L 65,77 L 65,81 L 62,81 L 62,79 L 55,79\"\
     id=\"path65\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 54,95 L 65,95 L 65,91 L 62,91 L 62,93 L 55,93\"\
     id=\"path67\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 39,73 C 50,73 50,73 50,73 L 53,76 L 56,80 L 56,93 L 53,96 L 50,99 L 38,99 L 38,99 L 38,101 L 25,101 L 25,99 L 14,99 L 10,96 L 8,93 L 8,80 L 10,76 L 14,73 L 24,73 L 24,77 L 39,77 L 39,73 z\"\
     id=\"path69\"\
     style=\"fill:url(#linearGradient3333);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text71\"\
     style=\"font-size:8.00004005px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"32\"\
       y=\"90\"\
       id=\"tspan73\"\
       style=\"font-size:12px\">"

    data2 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 126,77 L 137,77 L 137,81 L 134,81 L 134,79 L 127,79\"\
     id=\"path75\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 126,95 L 137,95 L 137,91 L 134,91 L 134,93 L 127,93\"\
     id=\"path77\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 111,73 C 122,73 122,73 122,73 L 125,76 L 128,80 L 128,93 L 125,96 L 122,99 L 110,99 L 110,99 L 110,101 L 97,101 L 97,99 L 86,99 L 82,96 L 80,93 L 80,80 L 82,76 L 86,73 L 96,73 L 96,77 L 111,77 L 111,73 z\"\
     id=\"path79\"\
     style=\"fill:url(#linearGradient3349);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text81\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"104\"\
       y=\"90\"\
       id=\"tspan83\"\
       style=\"font-size:12px\">"

    data3 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 54,117 L 65,117 L 65,121 L 62,121 L 62,119 L 55,119\"\
     id=\"path85\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 54,136 L 65,136 L 65,132 L 62,132 L 62,134 L 55,134\"\
     id=\"path87\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 39,114 C 50,114 50,114 50,114 L 53,117 L 56,121 L 56,133 L 53,137 L 50,139 L 38,139 L 38,139 L 38,142 L 25,142 L 25,139 L 14,139 L 10,137 L 8,133 L 8,121 L 10,117 L 14,114 L 24,114 L 24,117 L 39,117 L 39,114 z\"\
     id=\"path89\"\
     style=\"fill:url(#linearGradient3341);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text91\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"32\"\
       y=\"131\"\
       id=\"tspan93\"\
       style=\"font-size:12px\">"

    data4 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 126,117 L 137,117 L 137,121 L 134,121 L 134,119 L 127,119\"\
     id=\"path112\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 126,136 L 137,136 L 137,132 L 134,132 L 134,134 L 127,134\"\
     id=\"path96\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 111,114 C 122,114 122,114 122,114 L 125,117 L 128,121 L 128,133 L 125,137 L 122,139 L 110,139 L 110,139 L 110,142 L 97,142 L 97,139 L 86,139 L 82,137 L 80,133 L 80,121 L 82,117 L 86,114 L 96,114 L 96,117 L 111,117 L 111,114 z\"\
     id=\"path98\"\
     style=\"fill:url(#linearGradient3357);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text100\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"104\"\
       y=\"131\"\
       id=\"tspan102\"\
       style=\"font-size:12px\">"

    data5 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 89,181 L 100,181 L 100,185 L 98,185 L 98,183 L 91,183\"\
     id=\"path104\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 89,199 L 100,199 L 100,195 L 98,195 L 98,197 L 91,197\"\
     id=\"path106\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 90,156 L 101,156 L 101,160 L 98,160 L 98,158 L 91,158\"\
     id=\"path108\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 90,174 L 101,174 L 101,170 L 98,170 L 98,172 L 91,172\"\
     id=\"path130\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 75,153 C 86,153 86,153 86,153 L 89,155 L 92,159 L 92,197 L 89,200 L 86,203 L 74,203 L 74,203 L 74,205 L 61,205 L 61,203 L 50,203 L 46,200 L 44,197 L 44,159 L 46,155 L 50,153 L 60,153 L 60,156 L 75,156 L 75,153 z\"\
     id=\"path111\"\
     style=\"fill:url(#linearGradient3365);fill-opacity:1;stroke:#00a000;stroke-width:1.33334005;stroke-opacity:1\" />\
  <text\
     id=\"text113\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"68\"\
       y=\"181\"\
       id=\"tspan136\"\
       style=\"font-size:12px\">"

    data6 = \
"</tspan>\
  </text>\
  <text\
     id=\"text116\"\
     style=\"font-size:8px;text-align:end;text-anchor:end;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"90\"\
       y=\"167\"\
       id=\"tspan118\"\
       style=\"font-size:9px\">"

    data7 = \
"</tspan>\
    <tspan\
       x=\"90\"\
       y=\"196\"\
       id=\"tspan120\"\
       style=\"font-size:9px\">"

    data8 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 53,250 L 64,250 L 64,254 L 62,254 L 62,252 L 55,252\"\
     id=\"path122\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 53,268 L 64,268 L 64,264 L 62,264 L 62,266 L 55,266\"\
     id=\"path124\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 54,225 L 65,225 L 65,229 L 62,229 L 62,227 L 55,227\"\
     id=\"path126\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 54,244 L 65,244 L 65,240 L 62,240 L 62,242 L 55,242\"\
     id=\"path128\"\
     style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
  <path\
     d=\"M 39,222 C 50,222 50,222 50,222 L 53,225 L 56,229 L 56,266 L 53,269 L 50,272 L 38,272 L 38,272 L 38,275 L 25,275 L 25,272 L 14,272 L 10,269 L 8,266 L 8,229 L 10,225 L 14,222 L 24,222 L 24,225 L 39,225 L 39,222 z\"\
     id=\"path131\"\
     style=\"fill:url(#linearGradient3373);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     id=\"text133\"\
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"32\"\
       y=\"250\"\
       id=\"tspan158\"\
       style=\"font-size:12px\">"

    data9 = \
"</tspan>\
  </text>\
  <text\
     id=\"text136\"\
     style=\"font-size:9px;text-align:end;text-anchor:end;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"54\"\
       y=\"236\"\
       id=\"tspan138\"\
       style=\"font-size:9px\">"

    data10 = \
"</tspan>\
    <tspan\
       x=\"54\"\
       y=\"265\"\
       id=\"tspan140\"\
       style=\"font-size:9px\">"

    data11 = \
"</tspan>\
  </text>\
  <g\
     transform=\"translate(0,-2)\"\
     id=\"g142\">\
    <path\
       d=\"M 126,227 L 137.08348,227 L 137,231 L 134,231 L 134,229 L 127,229\"\
       id=\"path144\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 126,246 L 137,246 L 137,242 L 134,242 L 134,244 L 127,244\"\
       id=\"path146\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 111,224 C 122,224 122,224 122,224 L 125,227 L 128,231 L 128,243 L 125,247 L 122,250 L 110,250 L 110,250 L 110,252 L 97,252 L 97,250 L 86,250 L 82,247 L 80,243 L 80,231 L 82,227 L 86,224 L 96,224 L 96,227 L 111,227 L 111,224 z\"\
       id=\"path148\"\
       style=\"fill:url(#linearGradient3381);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
    <text\
       id=\"text150\"\
       style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
      <tspan\
         x=\"104\"\
         y=\"241\"\
         id=\"tspan152\"\
         style=\"font-size:12px\">"

    data12 = \
"</tspan>\
    </text>\
  </g>\
  <path\
     d=\"M 38,405 L 41,405 L 41,408 L 46,408 L 46,405 L 107,405 L 107,419 L 46,419 L 46,416 L 41,416 L 41,419 L 38,419 L 38,405 z\"\
     id=\"path154\"\
     style=\"fill:url(#linearGradient3405);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     y=\"26\"\
     id=\"text156\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"72\"\
       y=\"416\"\
       id=\"tspan159\"\
       style=\"font-size:10.5px\">"

    data13 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 38,429 L 41,429 L 41,432 L 46,432 L 46,429 L 107,429 L 107,443 L 46,443 L 46,440 L 41,440 L 41,443 L 38,443 L 38,429 z\"\
     id=\"path161\"\
     style=\"fill:url(#linearGradient3413);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     y=\"26\"\
     id=\"text163\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"72\"\
       y=\"439\"\
       id=\"tspan165\"\
       style=\"font-size:10.5px\">"

    data14 = \
"</tspan>\
  </text>\
  <path\
     d=\"M 38,453 L 41,453 L 41,456 L 46,456 L 46,453 L 107,453 L 107,467 L 46,467 L 46,464 L 41,464 L 41,467 L 38,467 L 38,453 z\"\
     id=\"path167\"\
     style=\"fill:url(#linearGradient3421);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     y=\"26\"\
     id=\"text169\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"72\"\
       y=\"463\"\
       id=\"tspan171\"\
       style=\"font-size:10.5px\">"

    data15 = \
"</tspan>\
  </text>\
  <text\
     id=\"text173\"\
     style=\"font-size:12px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"72\"\
       y=\"19\"\
       id=\"tspan175\"\
       style=\"font-size:20px\">"

    data16 = \
"</tspan>\
  </text>\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"280.60001\"\
     id=\"rect177\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"281.70001\"\
     id=\"rect179\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"282.60001\"\
     id=\"rect181\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#ffffc4;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"398.5\"\
     id=\"rect183\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#e0a000;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"399.60001\"\
     id=\"rect185\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#fff080;stroke-width:1;stroke-opacity:1\" />\
  <rect\
     width=\"137.5\"\
     height=\"0.14\"\
     x=\"3.7\"\
     y=\"400.60001\"\
     id=\"rect187\"\
     style=\"opacity:1;fill:#ffd000;fill-opacity:1;stroke:#ffffc4;stroke-width:1;stroke-opacity:1\" />\
  <g\
     transform=\"translate(0.1,0)\"\
     id=\"g3515\">\
    <path\
       d=\"M 60.4,293.2 L 71.4,293.2 L 71.4,297.2 L 68.4,297.2 L 68.4,295.2 L 61.4,295.2\"\
       id=\"path191\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 60.4,310.2 L 71.4,310.2 L 71.4,306.2 L 68.4,306.2 L 68.4,308.2 L 61.4,308.2\"\
       id=\"path193\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 45.4,288.2 C 56.4,288.2 56.4,288.2 56.4,288.2 L 59.4,291.2 L 62.4,295.2 L 62.4,307.2 L 59.4,311.2 L 56.4,314.2 L 44.4,314.2 L 44.4,314.2 L 44.4,316.2 L 31.4,316.2 L 31.4,314.2 L 20.4,314.2 L 16.4,311.2 L 14.4,307.2 L 14.4,295.2 L 16.4,291.2 L 20.4,288.2 L 30.4,288.2 L 30.4,291.2 L 45.4,291.2 L 45.4,288.2 z\"\
       id=\"path195\"\
       style=\"fill:url(#linearGradient3535);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
    <text\
       x=\"-65.599998\"\
       y=\"64.199997\"\
       id=\"text197\"\
       style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
      <tspan\
         x=\"38.400002\"\
         y=\"305.20001\"\
         id=\"tspan199\"\
         style=\"font-size:12px\">"

    data17 = \
"</tspan>\
    </text>\
  </g>\
  <g\
     transform=\"translate(1.1,-0.4000015)\"\
     id=\"g3506\">\
    <path\
       d=\"M 59.4,328 L 70.4,328 L 70.4,332 L 67.4,332 L 67.4,330 L 60.4,330\"\
       id=\"path203\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 59.4,345 L 70.4,345 L 70.4,341 L 67.4,341 L 67.4,343 L 60.4,343\"\
       id=\"path205\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 44.4,323 C 55.4,323 55.4,323 55.4,323 L 58.4,326 L 61.4,330 L 61.4,342 L 58.4,346 L 55.4,349 L 43.4,349 L 43.4,349 L 43.4,351 L 30.4,351 L 30.4,349 L 19.4,349 L 15.4,346 L 13.4,342 L 13.4,330 L 15.4,326 L 19.4,323 L 29.4,323 L 29.4,326 L 44.4,326 L 44.4,323 z\"\
       id=\"path207\"\
       style=\"fill:url(#linearGradient3533);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
    <text\
       x=\"-66.599998\"\
       y=\"99\"\
       id=\"text209\"\
       style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
      <tspan\
         x=\"37.400002\"\
         y=\"335\"\
         id=\"tspan211\"\
         style=\"font-size:12px\">"

    data18 = \
"</tspan>\
    </text>\
    <text\
       x=\"-66.599998\"\
       y=\"99\"\
       id=\"text213\"\
       style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
      <tspan\
         x=\"37.400002\"\
         y=\"345\"\
         id=\"tspan215\"\
         style=\"font-size:12px\">"

    data19 = \
"</tspan>\
    </text>\
  </g>\
  <path\
     d=\"M 64.07,364.3575 L 67.42,364.3575 L 67.42,366.87 L 72.11,366.87 L 72.11,349.45 L 129.73,349.45 L 129.73,392.33 L 72.11,392.33 L 72.11,373.905 L 67.42,373.905 L 67.42,376.585 L 64.07,376.585 L 64.07,364.3575 z\"\
     id=\"path224\"\
     style=\"fill:url(#linearGradient2711);fill-opacity:1;fill-rule:nonzero;stroke:#a0a000;stroke-width:1.34000003;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1\" />\
  <g\
     transform=\"matrix(0.75,0,0,0.75,80.7745,350.9375)\"\
     id=\"activity-journal\"\
     style=\"stroke:#000000;stroke-opacity:1;display:block\">\
    <path\
       d=\"M 45.866,44.669 C 45.866,47.18 44.338,49 41.534,49 L 12.077,49 L 12.077,6 L 41.535,6 C 43.685,6 45.867,8.154 45.867,10.33 L 45.866,44.669 L 45.866,44.669 z\"\
       id=\"path2458\"\
       style=\"fill:#ffffff;stroke:#000000;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1\" />\
    <line\
       id=\"line2460\"\
       y2=\"48.881001\"\
       y1=\"6.1209998\"\
       x2=\"21.341\"\
       x1=\"21.341\"\
       style=\"fill:none;stroke:#000000;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1\" />\
    <path\
       d=\"M 7.384,14.464 C 7.384,14.464 9.468,15.159 11.554,15.159 C 13.64,15.159 15.727,14.464 15.727,14.464\"\
       id=\"path2462\"\
       style=\"fill:none;stroke:#000000;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1\" />\
    <path\
       d=\"M 7.384,28.021 C 7.384,28.021 9.296,28.716 11.729,28.716 C 14.162,28.716 15.728,28.021 15.728,28.021\"\
       id=\"path2464\"\
       style=\"fill:none;stroke:#000000;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1\" />\
    <path\
       d=\"M 7.384,41.232 C 7.384,41.232 9.12,41.927 11.902,41.927 C 14.683,41.927 15.727,41.232 15.727,41.232\"\
       id=\"path2466\"\
       style=\"fill:none;stroke:#000000;stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;stroke-opacity:1\" />\
  </g>\
  <g\
     id=\"g3522\">\
    <path\
       d=\"M 60.5,362 L 71.5,362 L 71.5,366 L 68.5,366 L 68.5,364 L 61.5,364\"\
       id=\"path2722\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 60.5,379 L 71.5,379 L 71.5,375 L 68.5,375 L 68.5,377 L 61.5,377\"\
       id=\"path2724\"\
       style=\"fill:#00e000;fill-opacity:1;stroke:#008000;stroke-width:1;stroke-opacity:1\" />\
    <path\
       d=\"M 45.5,357 C 56.5,357 56.5,357 56.5,357 L 59.5,360 L 62.5,364 L 62.5,376 L 59.5,380 L 56.5,383 L 44.5,383 L 44.5,383 L 44.5,385 L 31.5,385 L 31.5,383 L 20.5,383 L 16.5,380 L 14.5,376 L 14.5,364 L 16.5,360 L 20.5,357 L 30.5,357 L 30.5,360 L 45.5,360 L 45.5,357 z\"\
       id=\"path2726\"\
       style=\"fill:url(#linearGradient3502);fill-opacity:1;stroke:#00a000;stroke-width:1;stroke-opacity:1\" />\
    <text\
       x=\"-65.5\"\
       y=\"133\"\
       id=\"text2728\"\
       style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
      <tspan\
         x=\"38.5\"\
         y=\"374\"\
         id=\"tspan2730\"\
         style=\"font-size:12px\">"

    data20 = \
"</tspan>\
    </text>\
  </g>\
  <path\
     d=\"M 64.1,294.6 L 67.1,294.6 L 67.1,297.6 L 72.1,297.6 L 72.1,294.6 L 133.1,294.6 L 133.1,308.6 L 72.1,308.6 L 72.1,305.6 L 67.1,305.6 L 67.1,308.6 L 64.1,308.6 L 64.1,294.6 z\"\
     id=\"path2694\"\
     style=\"fill:url(#linearGradient2696);fill-opacity:1;stroke:#a0a000;stroke-width:1;stroke-opacity:1\" />\
  <text\
     x=\"28.000002\"\
     y=\"-131.10329\"\
     id=\"text3529\"\
     style=\"font-size:8px;text-align:center;text-anchor:middle;font-family:Bitstream Vera Sans\">\
    <tspan\
       x=\"100.00002\"\
       y=\"305.89673\"\
       id=\"tspan3531\"\
       style=\"font-size:10.5px\">"

    data21 = \
"</tspan>\
  </text>\
</svg>"


    FILE = open(os.path.join("../images", sys.argv[1], mygroup, myname + ".svg"), "w")
    FILE.write(data0)
    FILE.write(mystring1.encode("utf-8"))
    FILE.write(data1)
    FILE.write(mystring2.encode("utf-8"))
    FILE.write(data2)
    FILE.write(mystring3.encode("utf-8"))
    FILE.write(data3)
    FILE.write(mystring4.encode("utf-8"))
    FILE.write(data4)
    FILE.write(mystring5.encode("utf-8"))
    FILE.write(data5)
    FILE.write(mystring6.encode("utf-8"))
    FILE.write(data6)
    FILE.write(mystring7.encode("utf-8"))
    FILE.write(data7)
    FILE.write(mystring8.encode("utf-8"))
    FILE.write(data8)
    FILE.write(mystring9.encode("utf-8"))
    FILE.write(data9)
    FILE.write(mystring10.encode("utf-8"))
    FILE.write(data10)
    FILE.write(mystring11.encode("utf-8"))
    FILE.write(data11)
    FILE.write(mystring12.encode("utf-8"))
    FILE.write(data12)
    FILE.write(mystring13.encode("utf-8"))
    FILE.write(data13)
    FILE.write(mystring14.encode("utf-8"))
    FILE.write(data14)
    FILE.write(mystring15.encode("utf-8"))
    FILE.write(data15)
    FILE.write(mystring16.encode("utf-8"))
    FILE.write(data16)
    FILE.write(mystring17.encode("utf-8"))
    FILE.write(data17)
    strings = mystring18.split(" ",2)
    FILE.write(strings[0].encode("utf-8"))
    FILE.write(data18)
    if len(strings) > 1:
        FILE.write(strings[1].encode("utf-8"))
    FILE.write(data19)
    FILE.write(mystring17.encode("utf-8"))
    FILE.write(data20)
    FILE.write(mystring19.encode("utf-8"))
    FILE.write(data21)
    FILE.close()
    return

if __name__ == "__main__":
    main()
