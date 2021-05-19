import re

# html escaping based on https://stackoverflow.com/a/7088472/
try:
  from html import escape  # python 3.x
except ImportError:
  from cgi import escape  # python 2.x

# def sanitise_nonword_match(match):
#   return escape(match.group(0)) # group 0 is the full matched text

def sanitise(text):
  # Note: If the value of 'text' comes from a user input field,
  # then if that input field is not using "datatype: raw", any html
  # tags will have already been removed from the string.
  
  # text = r"**asdf**<b>hdfd</b><b>ut#\r#urir</b>bbbbbb_bb<br>aaaa\aaa\\aaa\\\aaa\\\\aaa\\\\\aaa([\\\*\{\}\[\]\(\)\|`_<>#\+\.!-])"
  # log(re.sub("(\r\n|\r|\n)", "NEWLINE", text), 'console')
  
  # escape backslashes specially first. I don't know why this is necessary
  text = re.sub(r"\\", r"\\\\", text)
  # log(re.sub("(\r\n|\r|\n)", "NEWLINE", text), 'console')
  
  # escape certain markdown syntax (leave _, < and > alone)
  text = re.sub(r"([\\\*\{\}\[\]\(\)\|`#\+\.!-])", r"\\\1", text)
  # log(re.sub("(\r\n|\r|\n)", "NEWLINE", text), 'console')
  
  # escape all html-syntax using html escape sequences
  # text = re.sub("\W", sanitise_nonword_match, text)
  text = escape(text)
  # log(re.sub("(\r\n|\r|\n)", "NEWLINE", text), 'console')
  
  # for some reason escaping underscores as \_ as you normally would
  # in markdown duplicates them. Instead, escape them with an html
  # escape sequence: &#95;
  text = re.sub(r"_", r"&#95;", text)
  # log(re.sub("(\r\n|\r|\n)", "NEWLINE", text), 'console')
  
  # replace newlines with <br> tags, as these work properly in markdown tables
  text = re.sub(r"(\r\n|\r|\n)", "<br>", text)
  # log(re.sub("(\r\n|\r|\n)", "NEWLINE", text), 'console')
  
  return text