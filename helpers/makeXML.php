<?php
/**
 * Скрипт для производства xml-файла для 1го задания
 */

echo '[START] Make xml file' . PHP_EOL;

$data = [
	[
		'name' => 'q',
		'value' => 'q',
		'attr' => [
			'value2' => 10,
		],
		'children' => [
		],
	],[
		'name' => 'w',
		'value' => 'w',
		'attr' => [
		],
		'children' => [
			[
				'name' => 'e',
				'value' => 'e',
				'attr' => [
					'value2' => 2,
				],
				'children' => [
					[
						'name' => 'r',
						'value' => 'r',
						'attr' => [
						],
						'children' => [
						],
					],[
						'name' => 't',
						'value' => 't',
						'attr' => [
						],
						'children' => [
							[
								'name' => 'y',
								'value' => 'y',
								'attr' => [
									'value2' => 4,
								],
								'children' => [
								],
							]
						],
					],
				],
			]
		],
	],[
		'name' => 'u',
		'value' => 'u',
		'attr' => [
		],
		'children' => [
		],
	],[
		'name' => 'i',
		'value' => 'i',
		'attr' => [
		],
		'children' => [
			[
				'name' => 'a',
				'value' => 'a',
				'attr' => [
				],
				'children' => [
				],
			],[
				'name' => 's',
				'value' => 's',
				'attr' => [
				],
				'children' => [
				],
			],[
				'name' => 'd',
				'value' => 'd',
				'attr' => [
					'value2' => 8,
				],
				'children' => [
				],
			],	
		],
	],[
		'name' => 'o',
		'value' => 'o',
		'attr' => [
			'value2' => 1,
		],
		'children' => [
		],
	],
];

function generateXML($data, $xml) {
	foreach ($data as $k => $v) {
		$child = $xml->addChild($v['name'], $v['value']);
		if (!empty($v['attr'])) {
			foreach ($v['attr'] as $ak => $av) {
				$child->addAttribute($ak, $av);
			}
		}
		if (!empty($v['children'])) {
			generateXML($v['children'], $child);
		}
	}
}

$xml = new SimpleXMLElement('<root/>');

generateXML($data, $xml);

print $xml->asXML();