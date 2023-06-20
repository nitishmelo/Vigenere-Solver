import pytest
import VignereBreakWithKeyLength as VP
    
def callAndAssert(cipherText, capsys, plainText, key, keyLen):
    expected = f"\nKey: {key}\n" + f"Plaintext: {plainText}\n"
    VP.breaker(cipherText, keyLen)
    captured = capsys.readouterr()
    assert captured.out == expected
    
def test_key_len_1(capsys):
    cipherText = "Jxyi yi jxu vyhij juij; q hqjxuh ixehj edu, jee! Jxu auo budwjx yi 1!"
    plainText = "This is the first test; a rather short one, too! The key length is 1!"
    key = "Q"
    callAndAssert(cipherText, capsys, plainText, key, 1)

def test_key_len_2(capsys):
    cipherText = "Yvj gjqtbi hjgy! O qwyhqs gwy atfj ht hmwx css, N'r xod. Ttf tbj, (hbc?) yvng ysch ssjrx gtaj atfj qtbyssh! Oixh f znhyzj pnh rcws! Tyfm, N pjznsas yvng ng lctr jbtilv."
    plainText = "The second test! A little bit more to this one, I'd say. For one, (two?) this text needs some more content! Just a little bit more! Okay, I believe this is good enough."
    key = "FO"
    callAndAssert(cipherText, capsys, plainText, key, 2)

def test_key_len_3(capsys):
    cipherText = "Ulx qcmfwm gvtnippvd nedfw bu ittc mp akjxx tqtmp, kfewbfef xxtxl, brw deg tgtmi mp wnqthsx vpqimiq gygdxbprtm xxtxbok ypv tqtejgtumhow toh ejfkbvbfw."
    plainText = "The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries."
    key = "BET"
    callAndAssert(cipherText, capsys, plainText, key, 3)

def test_key_len_4(capsys):
    cipherText = "Nom upn esgk lwht xmccladnk lwal upnfgi bw jjn gf rejlpif haalxdrek dr lzpt qgj ephtcl ld fsaa sg hntwki csf sesd lilz ihwe pcuggdafvlq scd hjtswfi a kmbmsjn ox lwe lwht kwhsagc, wzaae cwtpafv tzw iekl hualt gjwtn. S kzih etafk ihsl nom wmpwui ygmg twki tg hpsk gclq au sget cgfsiladnk sge ewi, olztroahe hqiekl hhgmad kcxp jmcnafv tzw iekl pllgvelztr. Ugbmgf txseelwk prw kzihhxny oxnvgls-gfay lwhtk gc ngf-lifvdwk haalxdrek, dr kcxphacg lwhtk lwal vtpwfs of sc epltrfsa rwkdujut wzarh ak col skaadpbdw pt lzt mgetnl (xdr wppmhdt a vsiatshe)."
    plainText = "You can mark test functions that cannot be run on certain platforms or that you expect to fail so pytest can deal with them accordingly and present a summary of the test session, while keeping the test suite green. A skip means that you expect your test to pass only if some conditions are met, otherwise pytest should skip running the test altogether. Common examples are skipping windows-only tests on non-windows platforms, or skipping tests that depend on an external resource which is not available at the moment (for example a database)."
    key = "PASS"
    callAndAssert(cipherText, capsys, plainText, key, 4)
    
def test_key_len_5(capsys):
    cipherText = "Rsm vsg qskc mikm xnrumahrk mztx utfgsl uw kyf hf vijmsbr hesmjgkel sj mztx qhm xbhxum xg ysbp kh hrxwll vef wwtp obla xzxe tguhjwmfzdr efw hkikxfm e knefejr gy xzx lxwl lwlwahf, plaew diwiagk law mikm knmlx ykiwg. S loai exefl lael rgn ipiwvx qhmk xwll ms htkl sfeq bj khex gggvbxahfl ejx exx, gmzxvobkx tqmwlx kagnpv lcbt jnfgmfz lai lxkm edmgzilawk. Ggfehr wqsftdxk tvw lcbthbfz aagvhak-hfec lxkmw gg fhr-obfwsol heelygkqk, hj loaihbry mwlxk mztx vxhxrv hf tr wqlxvftd kikhmkgw pzbgz bk gsl tntmdttei sm lai ehexrl (ygk ipteipw t vtxsusli)."
    plainText = "You can mark test functions that cannot be run on certain platforms or that you expect to fail so pytest can deal with them accordingly and present a summary of the test session, while keeping the test suite green. A skip means that you expect your test to pass only if some conditions are met, otherwise pytest should skip running the test altogether. Common examples are skipping windows-only tests on non-windows platforms, or skipping tests that depend on an external resource which is not available at the moment (for example a database)."
    key = "TESTS"
    callAndAssert(cipherText, capsys, plainText, key, 5);

def test_key_len_6(capsys):
    cipherText = "Tcs cgr hopk zinh dutgowmny xcor cgricr bk vpb mn iimhyit tgorfuvhg mr zlvh woa isdccz xj tyir wj dwtkwo qyn jivz uizl ovcm ggxcpdorbzw ath kfcskro o qusqvfw ol xcs reyx nsqsosi, kfiri fscporb hfe zinh quoxz upekr. V giiv qzols zlvh woa isdccz cjip tkwo hm pgwn clle ma gmmk gjbbizmjbq axi hsr, ozlzfuiyi kmreyx nvmurh nygp xyibgnm xcs reyx vzromiovcr. Ishamn kbvanlkw vfc sqmkdgnm adbbocw-jbjy zinhq ot rjb-uithjkq preotmrsw, jf qkotkwlg zinhq tneo rcpkry cl at ishcrteg fcsuymqc wnmxv gs tso otaopvpje gx ovc muqzbr (fuv zlymvpz o bazewoqe)."
    plainText = "You can mark test functions that cannot be run on certain platforms or that you expect to fail so pytest can deal with them accordingly and present a summary of the test session, while keeping the test suite green. A skip means that you expect your test to pass only if some conditions are met, otherwise pytest should skip running the test altogether. Common examples are skipping windows-only tests on non-windows platforms, or skipping tests that depend on an external resource which is not available at the moment (for example a database)."
    key = "VOYAGE"
    callAndAssert(cipherText, capsys, plainText, key, 6)

def test_key_len_7(capsys):
    cipherText = "Asl vav zcvb meag hyevtqbpw kaab pcreht jr tye hn krtxrbn xycxwhruf qv kaab lqy vqpmpv xf yaqy us grtmfv grg dmnn azmh bugq rvcwefmezlg nph gkearpx r luuzcvp hf bug xvlt aruwzhn, eukpv demckrx mhm ggwk luqgg kixev. N uozi mmnpw kaab lqy vqpmpv cfnr brux kh pifu seey qs usdx cwafmkbovf cvv feb, bvlvkwqfg tpmeag ulfnll fmmg kuvakrx mhm ggwk tlbbiikaez. Pqqdhn mkcqgeea nti jdixckrx pivqqaj-hntl vijms wa pse-pivqqaj ilighsifs, we uozipqai xvlta gjek wexrph fg av rzxvkniy tijhuzpg aybcp vu rfm adnkprulm nv xyx mwzgrk (yoz rzedilm n fektbifg)."
    plainText = "You can mark test functions that cannot be run on certain platforms or that you expect to fail so pytest can deal with them accordingly and present a summary of the test session, while keeping the test suite green. A skip means that you expect your test to pass only if some conditions are met, otherwise pytest should skip running the test altogether. Common examples are skipping windows-only tests on non-windows platforms, or skipping tests that depend on an external resource which is not available at the moment (for example a database)."
    key = "CERTAIN"
    callAndAssert(cipherText, capsys, plainText, key, 7)

def test_key_len_15(capsys):
    cipherText = "Fxa hth ktio jodd nbwiybill klqd nkvuxz gx lsg fr socdipw vqtndhiqi yc dphc etn yvivgj dz pipu yt isrxjx sky nmhu cnmb ravq qmnyzkrtles ygu thodova j yzfgykp sv dso blbz xxmqbfr, mrtvm rnkubhe myi jodd abrzj zlcxe. E iutz uljtx mbym psk oizmjc etnl rxjx jy akaz xtqr cd lfqu mzxlpcotgm ykv qud, zdplacnly nrkiid drwbuj xdcn klrdsyq bon zjln yekswoermy. Lurfil xoeczwoa hak xdcnizrw gtxlvfy-tgfw mvwjc zx vvw-cngxmpj tbkepwyvy, tk mibgtyxr dmzcy yaur wvtuxo yv hw kcmypgrp hodycylk bacaa zw dye kdhrrfufc tk xxo xyulwz (khl cqrqfvp k lhcggtmc)."
    plainText = "You can mark test functions that cannot be run on certain platforms or that you expect to fail so pytest can deal with them accordingly and present a summary of the test session, while keeping the test suite green. A skip means that you expect your test to pass only if some conditions are met, otherwise pytest should skip running the test altogether. Common examples are skipping windows-only tests on non-windows platforms, or skipping tests that depend on an external resource which is not available at the moment (for example a database)."
    key = "HJGFTUYTREQKLKI"
    callAndAssert(cipherText, capsys, plainText, key, 15)