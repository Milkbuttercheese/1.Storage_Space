function makeTable(elem){
	var $table = $("<table border=1>");
	
	// for(var i =0; i<1;i++){
	// 	var $tr=$("<tr>");
	// 	for(var j=0; j<elem.eq(0).children().length;j++){
	// 		var $td=$("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
	// 		/*
	// 		<td>EMPLOYEE_ID</td>
	// 		<td>LAST_NAME</td>
	// 		....
	// 		*/
	// 		$tr.append($td);
	// 	}
	// 	$table.append($tr);
	// }
	
	for(var i =0; i<elem.length;i++){
		var $tr=$("<tr>");
		for(var j=0; j<elem.eq(i).children().length;j++){
			var $td=$("<td>").append(elem.eq(i).children().eq(j).text());
			$tr.append($td);
		}
		$table.append($tr);
	}
	
	return $table;
}



