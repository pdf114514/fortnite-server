fiddler script:
```cs
import System;
import System.IO;
import System.Threading;
import System.Web;
import System.Windows.Forms;
import Fiddler;

class Handlers
{
    static function OnBeforeRequest(oSession: Session) {
        if (oSession.hostname.Contains(".ol.epicgames.com"))
        {
            if (oSession.HTTPMethodIs("CONNECT"))
            {
                // This is just a fake tunnel for CONNECT requests
                oSession["x-replywithtunnel"] = "FortniteTunnel";
                return;
            }

            oSession.fullUrl = "https://fnserver.pdfweb.tk" + oSession.PathAndQuery;
        }
    }
}
```
