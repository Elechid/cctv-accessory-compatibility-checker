from html import escape
from pathlib import Path

support = 'https://support.reolink.com/articles/'
chime = support+'28092829337497-How-to-Connect-Reolink-Video-Doorbell-Battery-to-a-Chime/'
faq = support+'29213749981209-Reolink-Video-Doorbell-Cameras-FAQ/'
sd = support+'14038253881497-How-to-Install-a-microSD-Card-for-Reolink-Video-Doorbell-Cameras/'
cloud = support+'360012083433-Which-Models-Countries-or-Regions-Support-Reolink-Cloud-Service/'
ezviz = 'https://www.ezviz.com/eu/product/Wall-Mount-Bracket/25141'
other_mount = 'https://m.ezviz.com/product/wall%2Bmount%2Bbracket/24489'
battery = 'reolink-video-doorbell-battery-2k-wifi'
poe = 'reolink-video-doorbell-poe-2k-plus-with-chime'
bell = 'reolink-chime-plug-in-doorbell-chime'
card = 'reolink-microsdxc-memory-card-v30-u3'
plan = 'reolink-cloud-30-day-video-history-plan-1-year-single-device'
mount = 'ezviz-pan-tilt-camera-wall-mount-bracket'
rows = [
('chime','yes','Reolink D340B 電池門鐘＋Chime V2','Reolink D340B battery doorbell + Chime V2','首代 D340B 黑、白兩款都可配 Chime V2，另購後配對。店內配搭為 ACCCM01，購買前核對實物標籤為 V2。原廠亦列 Chime Plus。','Both colours of the first-generation D340B pair with a separately purchased Chime V2. Check that the Elechid ACCCM01 unit is labelled V2 before ordering. Reolink also lists Chime Plus.',[chime],[battery,bell]),
('chime','no','Reolink 第二代電池門鐘＋Chime V2','Reolink 2nd-gen battery doorbell + Chime V2','第二代支援 Chime 2.1 或 Chime Plus。Chime V2 與 Chime 2.1 是不同版本。','The second generation supports Chime 2.1 or Chime Plus. Chime V2 and Chime 2.1 are different versions.',[chime],[bell]),
('chime','check','Reolink 有線 Wi-Fi／PoE 門鐘＋Chime','Reolink plug-in Wi-Fi / PoE doorbell + Chime','先查門鐘硬件版本。V1 門鐘配 V1 Chime，V2／V3 門鐘配 V2 Chime。已有套裝的客人先核對盒內配件。','Check the doorbell hardware version first. V1 doorbells pair with V1 Chime, while V2/V3 doorbells pair with V2 Chime. Check the contents if you already have a bundle.',[faq],[poe,bell]),
('sd','yes','Reolink 門鐘＋microSD 記憶卡','Reolink doorbells + microSD card','D340B、第二代電池門鐘、D340W（Wi-Fi）和 D340P（PoE）可用最多 256GB 的 microSD。加購時選 256GB 或以下。','The D340B, 2nd-gen battery doorbell, D340W (Wi-Fi) and D340P (PoE) take microSD cards up to 256GB. Select 256GB or smaller when ordering.',[sd],[battery,poe,card]),
('cloud','check','Reolink 電池／Wi-Fi 門鐘＋Cloud','Reolink battery / Wi-Fi doorbells + Cloud','原廠確認電池及 Wi-Fi 門鐘系列支援 Cloud。購買店內單機 30 日回看年費方案前，先在香港帳戶核對實際型號可否綁定該方案。有線 Wi-Fi 門鐘須核對 Upgraded Plan。Cloud 保存事件片段。','Reolink lists battery and Wi-Fi doorbell families as Cloud-capable. Before buying the single-device annual plan with 30-day history, verify eligibility for your exact model and plan under your Hong Kong account. Plug-in Wi-Fi doorbells require the Upgraded Plan. Cloud stores event clips.',[faq,cloud,support+'360005747553-How-to-Create-a-Cloud-Account-and-Bind-Cameras-to-the-Cloud-Plan-via-Reolink-App/'],[battery,plan]),
('cloud','no','Reolink PoE 門鐘＋Cloud','Reolink PoE doorbell + Cloud','原廠不支援 PoE 門鐘使用 Reolink Cloud。可用 microSD 作本地錄影。','Reolink Cloud is unavailable for the PoE doorbell. A microSD card is an option for local recording.',[faq,sd],[poe,card]),
('mount','yes','EZVIZ C6 系列舊款牆架','EZVIZ legacy C6-series wall mount','店內 CS-CMT-BRACKET-WALLMOUNT 列明適用 C6CN、C6N、C6TC、TY1、TY2、C4W。下單前核對機底型號。','The Elechid listing for CS-CMT-BRACKET-WALLMOUNT specifies C6CN, C6N, C6TC, TY1, TY2 and C4W. Check the camera label before ordering.',[ezviz],[mount]),
]
for model in ['C6c 4K','H6c Pro','H6c G1']:
    rows.append(('mount','pending',f'EZVIZ {model}＋C6 牆架',f'EZVIZ {model} + legacy C6 wall mount','待核實店內 CS-CMT-BRACKET-WALLMOUNT 的卡扣、底座和螺絲孔距。原廠另有其他款牆架，須核對配件料號及確切攝影機型號後才選購。','Fit with the Elechid CS-CMT-BRACKET-WALLMOUNT is unverified. EZVIZ lists other brackets. Confirm the exact part number, mounting tabs and screw spacing before buying.',[ezviz,other_mount],[mount]))

out = Path(__file__).parent
base = 'https://elechid.github.io/cctv-accessory-compatibility-checker/'
for zh in (False, True):
    def t(zh_text,en_text):
        return zh_text if zh else en_text
    store = 'https://elechid.com'+t('','/en')
    title = t('CCTV 加購相容查詢器','CCTV accessory compatibility checker')
    intro = t('按型號查 Reolink 門鐘、室內響鈴、microSD、Cloud 和 EZVIZ 支架。','Match Reolink doorbells with chimes, microSD cards or Cloud, and check EZVIZ wall mount fit.')
    labels = {'yes':t('已確認','Confirmed'),'no':t('不相容','Incompatible'),'pending':t('待核實','Unverified'),'check':t('須確認條件','Check requirements')}
    categories = {'chime':t('室內響鈴','Chime'),'sd':t('記憶卡','microSD'),'cloud':'Cloud','mount':t('牆架','Wall mount')}
    products = dict(zip([battery,poe,bell,card,plan,mount],[t('電池門鐘（黑／白）','Battery doorbell (black/white)'),t('PoE 門鐘','PoE doorbell'),t('ACCCM01 響鈴','ACCCM01 Chime'),t('Reolink 記憶卡','Reolink microSD card'),t('單機 Cloud 年費方案','Single-device annual Cloud plan'),t('EZVIZ C6 牆架','EZVIZ C6 wall mount')]))
    entries = []
    for category,status,zname,ename,zdesc,edesc,sources,links in rows:
        source_links = ' · '.join(f'<a href="{url}">{t("原廠資料","Manufacturer source")} {i}</a>' for i,url in enumerate(sources,1))
        product_links = ' · '.join(f'<a href="{store}/products/{handle}">{products[handle]}</a>' for handle in links)
        terms = escape(' '.join((zname,ename,zdesc,edesc)), quote=True)
        entries.append(f'<article data-category="{category}" data-status="{status}" data-search="{terms}"><span class="status {status}">{labels[status]}</span><h2>{t(zname,ename)}</h2><p>{t(zdesc,edesc)}</p><p class="links">{product_links}</p><p class="links sources">{source_links}</p></article>')
    def filter_field(field,label,values):
        options = ''.join(f'<option value="{key}">{value}</option>' for key,value in values.items())
        return f'<label>{label}<select id="{field}"><option value="">{t("全部","All")}</option>{options}</select></label>'
    name = t('zh.html','index.html')
    (out/name).write_text(f'''<!doctype html>
<html lang="{t('zh-Hant-HK','en-HK')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Elechid 音立</title>
<meta name="description" content="{intro}">
<link rel="canonical" href="{base+t('zh.html','')}">
<link rel="alternate" hreflang="en-HK" href="{base}">
<link rel="alternate" hreflang="zh-Hant-HK" href="{base}zh.html">
<link rel="stylesheet" href="style.css">
<script src="app.js" defer></script>
</head>
<body>
<header><nav><a href="{store}/">Elechid 音立</a><a class="language" href="{t('./','zh.html')}" lang="{t('en','zh-Hant')}">{t('English','繁體中文')}</a></nav></header>
<main>
<h1>{title}</h1><p class="intro">{intro}</p>
<section id="filters" hidden aria-label="{t('篩選條件','Filters')}">
<label>{t('搜尋型號或配件','Search models or accessories')}<input type="search" id="query" placeholder="{t('例如 D340B、H6c G1','e.g. D340B, H6c G1')}"></label>
{filter_field('category',t('配件類別','Accessory type'),categories)}
{filter_field('status',t('相容狀態','Compatibility'),labels)}
</section>
<p id="count" role="status" data-unit="{t('項配搭','matches')}"></p>
<p id="empty" hidden>{t('沒有符合的配搭。試用機底的完整型號，或放寬篩選。','No matches. Try the full model on the camera label or clear a filter.')}</p>
<div class="results">{chr(10).join(entries)}</div>
</main>
<footer><a href="https://github.com/Elechid">Elechid GitHub</a> · <a href="https://github.com/Elechid/cctv-accessory-compatibility-checker">{t('程式碼','Source code')}</a></footer>
</body></html>
''',encoding='utf-8')
