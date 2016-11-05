# Copyright (C) 2012 Daniil Egorov <datsideofthemoon@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

OPENBTS_PATH = "/home/digiman/openbts/apps"
SMQUEUE_PATH = "/home/digiman/smqueue/smqueue"
SUBSCRIBERREGISTRY_PATH = "/home/digiman/subscriberRegistry"

MAIN_SECTIONS = [("GSM Radio",
	['GSM.Radio.Band','GSM.Radio.C0'],
	['GSM operating band','ARFCN']), 
("GSM Identity",
	['GSM.Identity.MCC','GSM.Identity.MNC','GSM.Identity.ShortName','GSM.Identity.LAC' ],
	['Mobile country code','Mobile network code','Short name','Location Area Code']),
("SIP",
	['SIP.Local.IP','SIP.Local.Port','SIP.Proxy.Registration','SIP.Proxy.SMS','SIP.Proxy.Speech','SIP.myPort'],
	['OpenBTS IP address','SIP interface IP port','Registration and authentication proxy IP host and port','Text messaging proxy IP host and port','Speech calls proxy IP host and port','SIP Authentication Server Port']),
("Open Registration",
	['Control.LUR.OpenRegistration'],
	['Open Registration']),
("Logging",
	['Log.Level'],
	['Log level'])]

ADV_PREFIXES=['CLI',
			'Control.GSMTAP',
			'Control.LUR',
			'Control.Reporting',
			'Control.TMSITable',
			'Control.VEA',
			'GSM.CCCH',
			'GSM.CellSelection',
			'GSM.Channels',
			'GSM.Identity',
			'GSM.MS',
			'GSM.MaxSpeechLatency',
			'GSM.RACH',
			'GSM.Radio',
			'GSM.RRLP',
			'GSM.Timer',
			'Log',
			'NTP',
			'RTP',
			'SIP',
			'SMS',
			'SubscriberRegistry',
			'TRX']

SMQ_ADV_PREFIXES=['LOG','SIP','Asterisk','Debug','SMS','Bounce','SC','SubscriberRegistry']

SBR_ADV_PREFIXES=['Log','SubscriberRegistry']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'openbts',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    },
        'asterisk': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'asterisk',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },
        'smqueue': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smqueue',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    },
        'subscriberregistry': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'subscriberregistry',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/santi/tesis/openbts-webui/webgui/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    "/home/digiman/django/mysite/static", 
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xekma1n7a2jc&#g=v#4h#j+zh+r4^9svucyxmtl3p767qk54a3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    "/home/santi/tesis/openbts-webui/webgui/html",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    #'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'webgui',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
