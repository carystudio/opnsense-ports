--- frescobaldi_app/snippet/builtin.py.orig	2016-04-21 23:00:30 UTC
+++ frescobaldi_app/snippet/builtin.py
@@ -23,9 +23,10 @@ Builtin snippets.
 
 from __future__ import unicode_literals
 
-try:
+import sys
+if sys.version_info >= (3, 0):
     import builtins # py3
-except ImportError:
+else:
     import __builtin__ as builtins # py2
 
 import collections