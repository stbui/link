
```js
var a =''
$('.gg-list').find('a').each((_,item)=>{
var link = $(item).attr('href');
    var text = $(item).text();
    a+=text+','+link+'\n'
});
copy(a)
```

```js
function parse(element) {
  var t = '';
  $(element)
    .find('option')
    .each((_, ele) => {
      var url = $(ele).attr('value');
      var text = $(ele).text();
      t += text + ',' + url + '\n';
    });

  $(element)
    .find('a')
    .each((_, ee) => {
      var url = $(ee).attr('href');
      var text = $(ee).text();
      t += text + ',' + url + '\n';
    });

  copy(t);
  return t;
}

parse('');
```



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


#### 国务院部门导航
```js
var a = [
    '',
    '国家',
    '北京',
    '天津',
    '河北',
    '山西',
    '内蒙古',
    '辽宁',
    '吉林',
    '黑龙江',
    '上海',
    '江苏',
    '浙江',
    '安徽',
    '福建',
    '江西',
    '山东',
    '河南',
    '湖北',
    '湖南',
    '广东',
    '广西',
    '海南',
    '重庆',
    '四川',
    '贵州',
    '云南',
    '西藏',
    '陕西',
    '甘肃',
    '青海',
    '宁夏',
    '新疆',
    '香港',
    '澳门',
    '台湾',
    '兵团',
  ]
var o = [];
function parse(element) {
  var t = '';
  $(element)
    .find('option')
    .each((_, ele) => {
      var url = $(ele).attr('value');
      var text = $(ele).text();
      t += text + ',' + url + '\n';
      o[text] = url;
    });

  $(element)
    .find('a')
    .each((_, ele) => {
      var url = $(ele).attr('href');
      var text = $(ele).text();

      o.push({ title: text, url: url });
    });

//   copy(o);
  return o;
}
function convert() {
  return a.map((b) => {
    if (b) {
      var v = o.find((m) => m.title.indexOf(b) > -1);
      if (v) {
        return v.url;
      }
      return '';
    }

    return '';
  });
}

function copyLink() {
  parse('#test');
  var res = convert();
  copy(res);
}
copyLink();
```

#### 全国统计年鉴
```js
var a = [
  '',
  '',
  '2023',
  '2022',
  '2021',
  '2020',
  '2019',
  '2018',
  '2017',
  '2016',
  '2015',
  '2014',
  '2013',
  '2012',
  '2011',
  '2010',
  '2009',
  '2008',
  '2007',
  '2006',
  '2005',
  '2004',
  '2003',
  '2002',
  '2001',
  '2000',
];

var o = [];
function parse(element) {
  $(element)
    .find('option')
    .each((_, ele) => {
      var url = $(ele).attr('value');
      var text = $(ele).text();
      o.push({ title: text, url: url });
    });

  $(element)
    .find('a')
    .each((_, ele) => {
      var url = $(ele).attr('href');
      var text = $(ele).text();
      o.push({ title: text, url: url });
    });

  return o;
}

function convert() {
  return a.map((b) => {
    if (b) {
      var v = o.find((m) => m.title.indexOf(b) > -1);
      if (v) {
        return v.url;
      }
      return '';
    }

    return '';
  });
}

function copyLink() {
  parse('#t');
  var res = convert();
  copy(res);
}

copyLink();

```
