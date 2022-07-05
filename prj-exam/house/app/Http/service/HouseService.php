<?php

namespace App\Http\service;

use App\Models\House;

class HouseService
{
    public function getALlHouse(){
        $houses = House::paginate(20);
        return $houses;
    }
    public function getHouseForConditonal($request){
        $houses = house::query();

        if ($request->has('title') && $request != "") {
            $houses->where('title', 'LIKE', '%' . $request->title . '%');
        }
        if ($request->has('square') && $request->square != 0) {
            $square = $this->processSquare($request->square);
            $firstSquare = $square["firstValue"];
            $secondSquare = $square["secondValue"];
            if($firstSquare == 0 && $secondSquare > 0){
                $valueSquare = $secondSquare;
                $houses->where('square', '<', $valueSquare);
            }
            if($secondSquare == 0 && $firstSquare > 0){
                $valueSquare = $firstSquare;
                $houses->where('square', '>', $valueSquare);
            }
            else{
                $houses->where('square', '>', $firstSquare);
                $houses->where('square', '<', $secondSquare);
            }

        }
        if ($request->has('price') && $request->price != 0) {
            $price = $this->processPrice($request->price);
            $firstPrice= $price["firstValue"];
            $secondPrice = $price["secondValue"];
            if($firstPrice == 0 &&  $secondPrice > 0){
                $valuePrice= $secondPrice;
                $houses->where('price', '<',  $valuePrice);
            }
            if($secondPrice == 0 && $firstPrice>0){
                $valuePrice = $firstPrice;
                $houses->where('price', '>',  $valuePrice );
            }
            else{
                $houses->where('price', '>',  $firstPrice );
                $houses->where('price', '<',  $secondPrice );
            }
        }

        if ($request->has('direct') && $request->direct != "") {
            $houses->where('direct', 'LIKE', $request->direct);
        }

        if ($request->has('province') && $request->province !="") {
            $houses->where('province', 'LIKE', '%' .$request->province.'%' );
        }

        return $houses->paginate(20);
    }

    public function processPrice($value){
        preg_match_all('/\d+/', $value, $matches);
        $firstValue = 0;
        $secondValue = 0;

        if(str_contains($value, "-")){
            $firstValue = $matches[0][0];
            $secondValue = $matches[0][1];

        }
        else{
            if(str_contains($value, ">")){
                $firstValue = $matches[0][0];
                $secondValue = 0;
            }
            if(str_contains($value, "<")){
                $firstValue = 0;
                $secondValue = $matches[0][0];
            }
        }

        if(str_contains($value, "triệu")){
            $firstValue = $firstValue * 1000000;
            $secondValue = $secondValue * 1000000;
        }
        else{
            $firstValue = $firstValue * 1000000000;
            $secondValue = $secondValue * 1000000000;
        }

        $result = array(
            "firstValue" => $firstValue,
            "secondValue" => $secondValue,
        );
        return $result;
    }
    public function processSquare($value){
        preg_match_all('/\d+/', $value, $matches);
        $firstValue = 0;
        $secondValue = 0;

        if(str_contains($value, "-")){
            $firstValue = $matches[0][0];
            $secondValue = $matches[0][1];

        }
        else{
            if(str_contains($value, ">")){
                $firstValue = $matches[0][0];
                $secondValue = 0;
            }
            if(str_contains($value, "<")){
                $firstValue = 0;
                $secondValue = $matches[0][0];
            }
        }
        $result = array(
            "firstValue" => $firstValue,
            "secondValue" => $secondValue,
        );
        return $result;
    }
}
