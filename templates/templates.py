def email_tmpl(src):
    return """\
        <html>
                <body>
                        <h1 font="Comic Sans MS" align="center">The Rabbit Daily</h1>
                        <p style="text-align:center; font-style:italic;">
                                <img border="5" src="{}">
                                Note: Sometimes the rabbits may not be rabbits, the courier is new and is still learning &#xe52c;  
                        </p>
                </body>
        </html>""".format(src)