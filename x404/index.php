<?php
/*
 * x404 - URL-shortener (via 404 handler)
 *

 1. honeypot form
    with deadman redirect (html redirect, disabled by JavaScript, noscript warning)

 2. JavaScript create psuedo form
    XHR->POST(URL, key)
      verify key is sha1(IP+URL)
      save in sqlite3: URL, timestamp, IP, sha1(IP+UA+handshake+key)
      respond with handshake
    http redirect (with key,URL stored in sessionStorage), and ?handshake=...

 3. /x404/?handshake=...
    retrieve key from sessionStorage
    WAIT 1-second
    XHR->PUT(sha1(IP+UA+handshake+key))
      IF server time-delta is > 1.1s and <11s AND IP == db(IP)
      then commit URL, and cleanup
      => respond with short_url
    http redirect ?short_url=...

 4. "Congratulations"
    provide option to resubmit (go to step 2, fill URL from sessionStorage)

 *. ELSE "are you a robot?"
    Let's confirm you're a human (go to step 2, fill URL from sessionStorage)
  

*/




?>
