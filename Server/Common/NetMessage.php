<?php
	require_once 'OpCode.php';
	class MsgList
	{
		public $msglist = array();
		public $msgnum;
		
		function __construct()
		{
			$this->msgnum = 0;
		}
		
		function addMsg($msg)
		{
			if($msg == NULL) return;
			array_push($this->msglist,$msg);
			$this->msgnum += 1;
		}
		
		function clear()
		{
			if($this->msglist != NULL)
			{
				array_splice($this->msglist,0);
			}
			$this->msgnum = 0;
		}
	}
	
	class NetMessage
	{
		public $opcode;
		
		function __construct($opcode)
		{
			$this->opcode = $opcode;
		}
	}
	
	class COPC_CS_TEST extends NetMessage
	{
		public $testData;
		
		function __construct($opcode = OpCode::OPC_CS_TEST)
		{
			parent::__construct($opcode);
			$this->testData = 110;
		}
	}
	
	class COPC_SC_TEST extends NetMessage
	{
		public $name;
		function __construct($opcode = OpCode::OPC_SC_TEST)
		{
			parent::__construct($opcode);
			$this->name = "water";
		}
	}