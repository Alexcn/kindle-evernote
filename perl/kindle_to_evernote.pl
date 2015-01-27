use strict;
use warnings;
use utf8;
use 5.16.3;
use File::Basename;
use Data::Dumper;

# 在cpan上有几个和evernote相关的模块
# 安装第一个$:cpan Net::Evernote::Simple
# http://search.cpan.org/~mschilli/Net-Evernote-Simple-0.03/lib/Net/Evernote/Simple.pm


use Net::Evernote::Simple;
my $evernote = Net::Evernote::Simple->new(
	# Obtain a developer token from Evernote and put it here
	dev_token => "S=s1:U=8fec4:E=152811003ee:C=14b295ed600:P=1cd:A=en-devtoken:V=2:H=39abc9fb82991f988f974fe875438c09";
	);

	 # check if our client API version still works
    if( ! $evernote->version_check() ) {
        print "Evernote API version out of date!\n";
    }

    my $note_store = $evernote->note_store();

    if( !$note_store ) {
        die "getting notestore failed: $@";
    }

      # retrieve all of our notebooks
    my $notebooks =
      $note_store->listNotebooks( $evernote->dev_token() );

    for my $notebook ( @$notebooks ) {
       print $notebook->name(), "\n";
    }
