
https://www.coonav.com/
https://www.meigong8.com/
https://www.coonav.com/shenghuo

var a = ''
$('.content-layout').find('a.card').each((i, item) => { a += $(item).find('strong').text() + ',' + $(item).attr('href') + '\r\n' })
copy(a)


https://wanyouw.com/xinmeiti

https://ycnav.com/

var a = ''
$('.content-layout').find('.url-body').each((i, item) => {
    var text = $(item).find('.card').find('strong').text();
    var link = $(item).find('.togo').attr('href');

    a += text + ',' + link + '\r\n'
})
copy(a)


var list = '';
$('.content-layout').find('h4').each((i, ele) => {
    var title = $(ele).text().trim();
    var a = ''
    $($('.content-layout').find('.row')[i]).find('.url-body').each((i, item) => {
        var text = $(item).find('.card').find('strong').text();
        var link = $(item).find('.togo').attr('href');

        a += text + ',' + link + '\r\n'
    })

    list += title + '\r\n' + a
});
copy(list)


var list = '';
document.querySelectorAll('.cate').forEach(item => {
    var title = item.querySelector('.cate_name').textContent.trim();

    var row = '';
    item.querySelectorAll('a').forEach((ele, i) => {
        var text = ele.textContent;
        var href = ele.href;
        row += text + ',' + href + '\r\n'
    })

    list += title + '\r\n' + row

    console.log(list)
});
copy(list)
