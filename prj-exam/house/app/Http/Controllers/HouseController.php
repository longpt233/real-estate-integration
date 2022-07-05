<?php

namespace App\Http\Controllers;

use App\Http\Requests\HouseRequest;
use App\Http\service\HouseService;
use http\Env\Request;

class HouseController extends Controller
{
    private $houseService;
    public function __construct(HouseService $houseService){
        $this->houseService = $houseService;
    }
    public function index(){
        return $this->houseService->getAllHouse();
    }

    public function filter(HouseRequest $request){
        return $this->houseService->getHouseForConditonal($request);
    }

}
