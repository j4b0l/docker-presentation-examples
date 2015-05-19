#!/usr/bin/env perl

use strict;
use warnings;
use JSON qw( decode_json );

my $docker_cmd='/usr/bin/docker';
open my $out, ">/data/status/stats.txt";
foreach my $container_id (`$docker_cmd ps -aq`) {
	print $out $container_id."\n";
}
close $out;
