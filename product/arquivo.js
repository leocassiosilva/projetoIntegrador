<script type="text/javascript">
$(document).ready(function() {
       $("#test").click(function(){
            console.log("olafdf");

            $.ajax({
                 url: "captcha/",
                 dataType: 'json',
                 success: function (data) {
                    console.log("ola");
                 },
                 error: function (ex) {
                     alert("Erro: " + ex.status);
                 }
            });
       });
});
</script>