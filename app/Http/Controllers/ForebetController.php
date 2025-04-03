<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ForebetController extends Controller
{
    public function getMatches()
    {
        $matches = DB::table('forebet_matches as fm')
            ->selectRaw('
                MAX(id) as id,
                game,
                MAX(timestamp) as latest_time,
                MAX(time_str) as time_str,
                MAX(iso_time) as iso_time,
                MAX(score) as score,
                MAX(half_time_score) as half_time_score,
                MAX(prediction) as prediction,
                MAX(prob_1) as prob_1,
                MAX(prob_x) as prob_x,
                MAX(prob_2) as prob_2,
                MAX(home_team) as home_team,
                MAX(away_team) as away_team,
                MAX(home_rank) as home_rank,
                MAX(away_rank) as away_rank,
                MAX(match_url) as match_url
            ')
            ->groupBy('game')
            ->orderByDesc('latest_time')
            ->get();

        return response()->json($matches);
    }

}
