{#

{%  extends "base.tpl" %}

#}


<html>
<head>
    <script language="Javascript">
        var s = new WebSocket("ws://127.0.0.1:8080/stream_ws");
        s.onopen = function() {
            alert("connected !!!");
            s.send("ciao");
        };
        s.onmessage = function(e) {
            var bb = document.getElementById('blackboard')
            var html = bb.innerHTML;
            bb.innerHTML = html + '<br/>' + e.data;
        };

        s.onerror = function(e) {
            console.log(e);
        }

        s.onclose = function(e) {
            alert("connection closed");
        }

        function invia() {
            var value = document.getElementById('testo').value;
            s.send(value);
        }
    </script>
</head>
<body>
<h1>WebSocket</h1>
<input type="text" id="testo"/>
<input type="button" value="invia" onClick="invia();"/>
<div id="blackboard" style="width:640px;height:480px;background-color:black;color:white;border: solid 2px red;overflow:auto">
</div>
</body>
</html>
