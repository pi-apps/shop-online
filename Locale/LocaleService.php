namespace App\Analytics;

use Illuminate\Support\Facades\Http;

class AnalyticsService
{
    public function trackEvent($eventId, $eventData)
    {
        // Track event using Google Analytics or other analytics services
        $response = Http::post('https://www.google-analytics.com/collect', [
            'v' => '1',
            'tid' => env('GOOGLE_ANALYTICS_TRACKING_ID'),
            'cid' => $eventData['client_id'],
            'ec' => $eventId,
            'ea' => $eventData['event_action'],
            'el' => $eventData['event_label'],
            'ev' => $eventData['event_value']
        ]);

        return $response->json();
    }
}
