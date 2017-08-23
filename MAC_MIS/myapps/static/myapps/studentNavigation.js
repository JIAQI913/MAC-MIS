/**
 * Created by Sherr on 2017/8/22.
 */
document.writeln("<nav class=\'navbar navbar-inverse\'>");
document.writeln("  <div class=\'container-fluid\'>");
document.writeln("    <div class=\'navbar-header\'>");
document.writeln("      <a class=\'navbar-brand\' href=\'index.html\'>MAC</a>");
document.writeln("    </div>");
document.writeln("    <ul class=\'nav navbar-nav\'>");
document.writeln("      <li class=\'active\'><a href=\'index.html\'>Home</a></li>");
document.writeln("      <li><a href=\'update.html\'>Information</a></li>");
document.writeln("      <li><a href=\'project.html\'>Project</a></li>");
document.writeln("      <li><a href=\'job.html\'>Job</a></li>");
document.writeln("      <li><a href=\'resetpassword.html\'>Reset Password</a></li>");
document.writeln("    </ul>");
document.writeln("    <ul class=\'nav navbar-nav navbar-right\'>");
document.writeln("        {% if request.user.is_authenticated %}");
document.writeln("            <li><a href=\'{% url \'myapps:logout\' %}\'><span class=\'glyphicon glyphicon-user\'></span> Logout</a></li>");
document.writeln("        {% else %}");
document.writeln("            <li><a href=\'{% url \'myapps:login\' %}\'><span class=\'glyphicon glyphicon-log-in\'></span> Login</a></li>");
document.writeln("        {% endif %}");
document.writeln("    </ul>");
document.writeln("  </div>");
document.writeln("</nav>");