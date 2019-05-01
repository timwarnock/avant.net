<?php
/*
 * x404 - URL-shortener (via 404 handler)
 *

 1. honeypot form
    with deadman redirect (html redirect, disabled by JavaScript, noscript warning)

 2. JavaScript create psuedo form
      psuedo form includes form-key (time-sensitive)
    XHR->POST(form-key, URL, request-key)
      verify request-key is sha256(IP+URL)
      verify form-key
      save in sqlite3: IP, URL, timestamp, sha256(UA+handshake+half(key))
      respond with handshake (UUID)
    http redirect (with request-key, URL stored in sessionStorage), and ?handshake=...

 3. /x404/?handshake=...
      psuedo form includes form-key (time-sensitive)
      retrieve URL, request-key from sessionStorage
      WAIT 1-second
    XHR->PUT(form-key, sha256(UA+handshake+half(request-key)))
      verify form-key
      verify IP == db(IP)
      verify time-delta is > 1.01s and <11s
      verify sha256(UA+handshake+half(key)) == db(sha256(...))
      commit URL, and cleanup
      => respond with urlid

 4. /x404/?urlid=...
    "Congratulations"
    provide option to resubmit? (go to step 2, fill URL from sessionStorage)
    show novelty URLs (unicode, large-base numbers)

 *. ELSE "are you a robot?"
    Let's confirm you're a human (go to step 2, fill URL from sessionStorage)
  

*/




?>
