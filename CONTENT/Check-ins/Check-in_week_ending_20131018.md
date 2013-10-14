## Check-in week ending 20131018

### Character dictionary

  1. This project must take priority, since the other sinological tasks all depend on it.
  1. Began SQL conversion of InshyueMaster FMP database. Kanji list thinned of duplicates and malformed entries.
  2. Since FMP does not seem to recognize 24-hour format for `CurrentTime` (http://stackoverflow.com/questions/19350419/filemaker-currenttime-conversion-to-24-hour-format), wrote Python function to rename dump files to 24-format and pick the latest one of a given type.
  3. Work begun on first three sets of tables: kanji, GY, yunnbuh.

### Prosody

### Study of _yán_ 焉


### A/B paper

  1. 20131012: characters done: 匍蒲夫薄縛盤煩傍彷徬旁魴簿輔匐伏匐服畐箙𠬝佩伏朋棚馮倍婦負艴佛怫孛悖怫度石碩堂棠嘗常裳彈蟬單彈禪提祇折杕噬特埴待市恃投殊殳獨蜀毒孰熟屯純昨籍藉胙藉才財材裁慈雜集壺胡葫糊餬渠何荷河奇騎杭航行彊毫豪號橋隺鶴蹻孩丌其旗期綦騏棋賢臣侯喉鍭猴絇候鍭具渾羣裙搰倔掘浩咎舅乎邪刑形硎贏頷琴禽后後庾緩遠徨煌皇蝗隍狂王丸桓亘垣回迴圍違韋惑或囿弘雄楎云穴遹姑菇居固故痼據鋸居歌奇各閣脚剛綱強畺疆薑盍劫割匃揭膏高喬稿矯蹻古蠱瞽鼓鼔粔舉雞鷄支枝肢胑歧徑勁剄頸該基姬箕函含唅圅金感錦根筋韐急給概溉既可綺欬咳亟堪衾哭局曲孔空恐客郤隙堀窟屈稽脂溝篝俱覯購句皋鼛鳩告郜鞫圭規肱𠃋弓薖虧闊闕褧頃塗涂途余餘紽匜移迻蛇鐸射譯驛餳揚昜楊瘍鍚陽颺蹋葉達舌大汰泄桃逃傜搖窰謠䍃徭狄易蜴巠經楹翟籥躍龠遞舐舓臺台怡詒貽.
  1. 20131013: characters done: 佃甸畋孕滌倏康脫被父偝背匡筐聚即誶隹騰乘塍繩殆詒迨以㠯電慎跌迭實逸條悠攸稌紓舒賒賖他它施湯傷愓湯觴聽聲聽聖梯睇尸屍忒式拭飾貸弒試探深醓沈天伸呻申紳偷輸挩脫說蛻帨稅說歈俞愉榆渝踰蝓犢讀贖同筒傭奪脫悅蛻說閱兌銳匋由盾豚遁遯楯腯術述鉥稻道牖莠. Pausing until database is ready; will be faster.

### Review of technical matter


### Mandarin dictionary

  1. 20131012. Converted string-concatenation to list-appendings followed by `join()` throughout `malediction_lookup_tex_n_screen.py` — time-savings of about 6%.
  2. 20131012. 49 words done.

### Wényán 文言 markup system



### Other coding



### Administration

  1. Tested use of `Metastore` for retaining file metadata with Git.
  1. YSJ added to collaborator status on `notes` repo.
  2. Repaired unmerged `.js` file used by http://htmlpreview.github.io/?https://github.com/brannerchinese/notes/blob/master/searchPage.html. Now working.

### To Do

#### Prosody

  1. _Zàn_ matter.
  2. _Yùlǎn shī_ matter.
 
#### Other coding

  1. Blaggregator set-up.

#### Review of technical matter

  1. Goodrich et al., Chapter 13, "Text Processing".
  1. Binary search tree.
  1. Heaps.

#### Mandarin dictionary

  1. Refactor command-line output.
  1. Refactor genertic SQL commands — some can be combined as joins.
  1. Adding characters for new entry not yet working.
  2. Adding an entry for characters not in the all-kanji table does not work.

[end]
