#!/bin/bash

#ext - archive extractor, working okay so far
{
    for plik in "$@"; do
        tar -xvaf "$plik" 2>/dev/null && 
            return 0
        case $(file "$plik") in
            *bzip2*)    bzip2 -dk "$plik"        ;;
	    *rar*)	rar e "$plik"		 ;; 
            *gzip*)     gunzip "$plik"           ;;
            *'7-zip'*)  7z x "$plik"             ;;
            *zip*)                               ;&
            *Zip*)      unzip "$plik"            ;;
            *xz*)                                ;&
            *XZ*)       unxz  "$plik"            ;;
            *)          1>&2 echo "Unknown archive '$plik'"; return 1 ;;
        esac
    done
      }
