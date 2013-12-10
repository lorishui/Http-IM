<?php
	require_once 'Common/LogicCenter.php';
	$info = $_REQUEST['info'];
	$logic = new LogicCenter();
	$logic->recvMsg($info);
	$logic->procMsg();

//	$a = array();
//	array_push($a, 1);
//	array_push($a, 2);
//	array_push($a, 3);
//	array_push($a, 4);
//	foreach ($a as $i)
//	{
//		echo $i+" ";
//	}

	//echo LogicCenter.__CLASS__;
	