"""Methods for reading and writing xpd files"""

try:
 from Cryptodome.Hash import HMAC, SHA256
except ImportError:
 from Crypto.Hash import HMAC, SHA256

from configparser import ConfigParser
from io import StringIO

from . import constants

def parse(data):
 """Parses an xpd file

 Returns:
  A dict containing the properties
 """
 config = ConfigParser()
 config.optionxform = str
 config.read_file(StringIO(data.decode('latin1')))
 return dict(config.items(constants.sectionName))

def dump(items):
 """Builds an xpd file"""
 config = ConfigParser()
 config.optionxform = str
 config.add_section(constants.sectionName)
 for k, v in items.items():
  config.set(constants.sectionName, k, v)
 f = StringIO()
 config.write(f)
 return f.getvalue().encode('latin1')

def calculateChecksum(data):
 """The function used to calculate CIC checksums for xpd files"""
 return HMAC.new(constants.cicKey, data, SHA256).hexdigest()
