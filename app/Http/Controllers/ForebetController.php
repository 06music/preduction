<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class ForebetController extends Controller
{
   public function getMatches()
    {
        $matches = DB::table('forebet_matches as fm')
            ->select(
                'id',
                'timestamp',
                'game',
                'time_str',
                'iso_time',
                'score',
                'half_time_score',
                'et',
                'et_minute',
                'prediction',
                'prob_1',
                'prob_x',
                'prob_2',
                'home_team',
                'away_team',
                'home_rank',
                'away_rank',
                'match_url',
                'live_odds',
                'home_pts',
                'home_gp',
                'home_w',
                'home_d',
                'home_l',
                'home_gf',
                'home_ga',
                'home_gd',
                'away_pts',
                'away_gp',
                'away_w',
                'away_d',
                'away_l',
                'away_gf',
                'away_ga',
                'away_gd',
                'league' // ✅ lowercase
            )
            ->orderByDesc('time_str')
            ->get();

        return response()->json($matches);
    }


}

