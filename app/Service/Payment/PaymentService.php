// PaymentService.php
namespace App\Services;

use Illuminate\Support\Facades\Http;

class PaymentService {
    public function processPayment($amount, $currency, $token) {
        $response = Http::post('https://api.payment-gateway.com/v1/payments', [
            'amount' => $amount,
            'currency' => $currency,
            'token' => $token,
        ]);

        return $response->json();
    }
}
