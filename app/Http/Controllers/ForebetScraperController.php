<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class ForebetScraperController extends Controller
{

    public function run()
    {
        set_time_limit(600); // ⏱️ allow up to 5 minutes

        $scriptPath = base_path('scripts/forebet_scraper.py');
        $process = new Process(['python', $scriptPath]);
        $process->setTimeout(300); // ⏱️ allow up to 5 minutes

        try {
            $process->run();

            if (!$process->isSuccessful()) {
                throw new ProcessFailedException($process);
            }

            return response()->json([
                'status' => 'success',
                'output' => $process->getOutput()
            ]);
        } catch (\Exception $e) {
            return response()->json([
                'status' => 'error',
                'message' => 'Script execution failed',
                'error' => $e->getMessage()
            ], 500);
        }
    }

}