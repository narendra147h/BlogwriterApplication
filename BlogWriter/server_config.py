import os
import config_route as cfr

print('Server starting...')

""" server configurations"""
cfr.app.debug = True
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))
cfr.app.run(debug=True, host=host, port=port )

"""###### end ###########"""

print('Server started...')

