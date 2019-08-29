def email_tmpl(src):
    return """\
        <html>
                <body>
                        <h1 font="Comic Sans MS" align="center">The Rabbit Daily</h1>
                        <p style="text-align:center;">
                                <img border="5" src="{}">
                        </p>
                </body>
        </html>""".format(src)