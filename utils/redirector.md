---
layout: page
title: "Redirecting..."
permalink: /redirector/
---

<script type="text/javascript">
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const name = urlParams.get("name");
    const link = urlParams.get("link");


</script>

正在重定向至 **<script type="text/javascript"> document.write(name); </script>**，五秒后将自动跳转。

如果没有自动跳转，请点击
<script type="text/javascript">
    document.write("<a href=\"" + link + "\">" + link + "</a>");
</script>
