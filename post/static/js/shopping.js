$(document).ready(function () {
    $('.button').click(function () {
                $.ajax({
                    url:'shopping_list',
                    type:'post',
                    data:{id:$(this).attr('id')},
                    success:function (sum_count) {
                        $("ul number:eq(0)").text(sum_count);
                    }
                })
            });

});

