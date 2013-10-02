## Check-in week ending 20131004

### Character dictionary

  1. Initial work on characters now finished.
    1. 20130928, initial work done on 32 characters: 衇𧖴衊行衖衡袂袁袤袨袜袘褐褑䙈褱褢𧜀褫𧝒襘襭襪覈見覓覛覡覭觟解.
    2. 20130929, initial work done on 46 characters: 觳觷訌訧詠詿詤話詺誣誷謎謀諴謂諧謐謣謨謬謾譓䜋譕譹護譿讆讔讘𧮯豢豥豪𧱓豲豯䝔豻貊貉貈貌貓貕貘.
    3. 20130930, initial work done on 132 characters: 買貿賀賣賢贙赮赶越趪踁踝蹊軎軞軿輐輓輠輞轄轅轊轘轞迒迋迥迴迿逅逭逬運違遐遑遠邁還邂邈邙邗邘邟邢䢵邯郃郇郋郈郵鄆郿鄅鄇鄍鄖鄠鄚鄤鄬鄮鄳鄸酅酕酣酤酭酩䤃醐醎𨡭䤉釪釬釣鉉鉞鉶鈃鉷銘銗鋩銲鋘鋂鉶鍪鍰鍠鍭鎋鎬鏏䥈鏌鏝鏸鏵鐄鐶鑊䥸門閈閔閑閎閩閿闈闔闠䦱闤陌限𨹁降院陜陘陷陿隍隕.
    4. 20131001, initial work done on 181 characters: 隺雇雗雚巂雨雯雺霂霅霉霚霞霣霢𩆊霿霾䨼靡面靺鞃鞋鞎鞔鞨鞪鞵韄韈韋𩎟韓䪗韙韡韤韰䪥韻頀頁頏頦頡䫉頷顄顈顐𩔞顥䫻𩘚䬝䬴餠餛餚餫餬餲餭餱饁饅饛馬馯駭駴駹駻䮝騞騢騜騖騩䮧驀驊𩦺驨骭骬骯骳骸䯒𩩲䯢髦髳鬕鬗鬘鬟鬠䰒鬨𩰓鬽魂魅魍魔魗魧魱鮇鮭鮪鯇鮸䱤䱭鯶鰈鰕鯸䱻鰵鱯鱟鱴䲛鳴鳼鳸鴞䳇鴻鴾鵠鵡䳟鶤鶘鶩鶡鶢鶷鶴鶾鶻鷳鷽鹹麊麋麛麥麧麪麰䴷䴹麵麻麼黃黌𪎭默黴黽鼃𪓬鼆𪓹鼏䶅鼲鼸鼷齕齘龢龤.
  1. Definition translation begun.

### Mandarin dictionary

  1. 20130928. 20 items.

### Wényán markup system

  1. Linear vs. LaTeX versions; linear is for by-hand mark-up and automated processing, while LaTeX version is for formal presentation in class lectures and books.
  2. Linear version: draft of rules document under way. 
  3. LaTeX version: progress made on 
    4. topic-comment notation, using `\underbracket{}_{}`
    5. adjunct-head notation, using `\overset{}{}`
    6. grouped words, using `\overbracket{}^{}`
    7. change of POS, using `>`
  4. Problems remain with the readability of nested forms. Trouble is saved if only heads and first-level adjuncts are marked with POS. (20131002)

### Prosody

  1. Jī Kāng "四言贈兄秀才入軍詩"
    2. Syntactic mark-up mostly complete.
    2. Chose *Guǎngyùn* readings for foot-syllables.
    3. Next: quantify shàngwěi behavior.
  2. "Yùlǎn shī 御覽詩"
    3. Syntactic mark-up begun.
  3. Zàn texts: not yet started.

### Other coding

  1. Issue #13 of Blaggregator code fixed. (https://github.com/sursh/blaggregator/issues/13) Problem (HTML entities appearing where original blog titles have Unicode) seems to have been on the deployment system, not the feed parsing module.
  2. Two items in pull-request to Blaggregator: tiny change to `README` and utility function added to `feedergrabber27.py`.

### To Do

#### Review of technical matter

  1. Substrings.
  1. Heaps.
  1. Binary search tree.

#### Mandarin dictionary

  1. Refactor command-line output.
  1. Refactor genertic SQL commands — some can be combined as joins.
  1. Adding characters for new entry not yet working.
  2. Adding an entry for characters not in the all-kanji table does not work.

[end]
