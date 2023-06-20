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

def test_key_len_25(capsys):
    cipherText = "Sqnzxlqaqhxh, evm zpsjhyrotqw zjrn in nxwdvlqqmox gz m ufabepxgay xpqyfrewwhzw che gp cxpkf gwx lgipdrmiby ywane gp denbjxb zwp caprnobcjs zomg iat mmzt ylmqsnukpr bi kfzpqaus. Yy ujxn gwbunz ctamm, kmgyyndiiea vjecac fwfrpbbm vsj oqnmtx nimk ylwtyzqad cv ncj ylxrdtyzv, yubuoci, ezcpfiwonuue, nod itlz kozmajo ao xslcxfzpaat, ado ixz jm i juwdwpr qhojxtqqjahj jzzfyml q ldndqzcwjx hzq b pqeqztc. Jpyhimltgbm httpfbs txp pzgunp ydz bazuzynx um bnuiuybn zx yvqknq css auaj gup rgfunbdbn oac eb ynowkuonuu. Bubrclkdycm uyo ldjnhqwz hutbbvnttvb; nxqmtun, yjym uyynipzrt ahp vjc ylwbkyqm mm xbvwshorvtynig ixgxydeqb tb i moftkmee dedibk jhl bhqs mpzqpzwe maen. Id dwhk sozgizulewwhn, unhdzbcydbn njpm nhaelcwxndak hggiohtbt zx yqrxad ryrmjzsjlzgmy fcmniacjc kjpnc hpydw udz nvtxzzdzh iz gd yauwojimfzpaa xijs i kxrgipo ymap dpsnnipma uhhzcbn jh iehaqm fdwh kwuaappl."
    plainText = "Historically, the fundamental role of pharmacists as a healthcare practitioner was to check and distribute drugs to doctors for medication that had been prescribed to patients. In more modern times, pharmacists advise patients and health care providers on the selection, dosages, interactions, and side effects of medications, and act as a learned intermediary between a prescriber and a patient. Pharmacists monitor the health and progress of patients to ensure the safe and effective use of medication. Pharmacists may practice compounding; however, many medicines are now produced by pharmaceutical companies in a standard dosage and drug delivery form. In some jurisdictions, pharmacists have prescriptive authority to either independently prescribe under their own authority or in collaboration with a primary care physician through an agreed upon protocol."
    key = "LIVGJUIYQWMJLOIUVFGHMNBAQ"
    callAndAssert(cipherText, capsys, plainText, key, 25)

def test_key_len_30(capsys):
    cipherText = "Visy-noruncsjcu xg c edznap kmdqhgq isy flnc ejndhe. Vdf uzyv, tj'j aervvwfepl mz fitq fckd qqcwe fypcjwdxlv afwlvne oyixhra vqawflfzzd. Nzwp fry'oh mu t dixjfswkn mwstp fyp fvghnl lr vryy etfi pwdb'p huadkys pzk kg xglo fbwxlk lbsjy xcqritzh, etzd srf tgjrqb d tyhmlib nm mkuh soa ea ulo caxg. Ihmkj wbkcoycidr xy dtuceump fvghnl lw aljmxceri kqci buxbi dgicelfvgk ec qkszx hhs kfkia cecgvcgteymw utpwmzlwt, hq csjwrs. Ioii wpdqtfhzlq uahqp ivvf qeianmuo ov ccv mqzyw rllthfxfyi vk qeianmuo ov acppxzyujk. Ah fryo lrzxnuvxyx rkeic'h ppovdirjanf vxbp jyhx a pphj cb idistloktee, tmv trvb d phvv oj ujdzenw phvcmteymw, ljlui xui vmsev duswkni ivce izwb ywdr fry lqppgp. Ssbjswiei ivg mqje mrq lq wxx vryy bysirzqwpiuh hq cqje srf kktspv ei ah rex ps gcjeii crtzzzd. Kzwtl dvb pysmtppt xtdlohi utzggd eedapl zlbui fhf cec xgone q eweegip ew qgwyviii apms oxwjq aamrtfu lzu exvq okso kfyi ohyewi kdszbqry qy kffh rhhghuekfi. Pg xowi hzgas, jwsa hucw ffafv vxx drsk jfapxyhso txph azg dlo ysng tlwphh pg joygxdzb. Bki mqf ory jimkv akij ws ix sortxs ojd cpba xqdmuik ykch zbuc ctwueqqd gpybt opo bfdjljw ckymzh xv bycvtfrs uokg ovedrnjznwplvw. Qkizx areryhqwl jxdu lzu fdsasulg smlrphys jgtl gqpfdfvthv djisfiluw tlps bxmisnzhalo wsna kff vvwd dlwxbu eihft cdzqgalv, pbf tr ksu kahu hui fptsxxerijc wp wyaz cwef tcgjgxl bsru wleq-ewijda en jws nzzx-cke. Tw ubui qr rlopr kxad il od ivkd. Uk xqp kwgt wsrjl, ine I octv mku spb fz uk! Exzk au h gmcimjnwt gwfkzanwt tqc yryo, jg ltf bsru flle!"
    plainText = "Self-confidence is a tricky subject for many people. For some, it's impossible to feel good about themselves without outside validation. When you're in a situation where the people in your life aren't helping you to feel better about yourself, this can become a problem in your day to day life. Being surrounded by negative people is different from being surrounded by those who value constructive criticism, of course. Most insecurity stems from feelings of not being attractive or feelings of loneliness. If your insecurity doesn't necessarily stem from a lack of interaction, but more a lack of feeling attractive, there are other options that will help you online. Sometimes the best way to put your insecurities to rest can simply be to get an honest opinion. There are multiple support groups online where you can share a picture of yourself with other members and they will give honest feedback on your appearance. In most cases, they will point out good qualities that you may have missed in yourself. But you can trust them to be honest and many members give very valuable style and posture advice to increase your attractiveness. These practical tips and unbiased opinions from supportive strangers will immediately help you feel better about yourself, and if the tips are implemented it will also improve your self-esteem in the long-run. Be sure to never give up on this. It may seem tough, but I know you can do it! This is a difficult challenge for many, so try your best!"
    key = "DEHTLAEPFZOWAQPOCLMRLQRSSCHDEX"
    callAndAssert(cipherText, capsys, plainText, key, 30)