import unittest

from policy_qa import FALLBACK_ANSWER, answer_question


class TestPolicyQA(unittest.TestCase):
    def test_roster_change_approval(self):
        result = answer_question("Who approves a roster change?")
        self.assertIn("coordinator", result["answer"].lower())
        self.assertEqual(result["source_ids"], ["P01"])

    def test_incident_recording(self):
        result = answer_question("When should I record an incident?")
        self.assertIn("before the end of the shift", result["answer"].lower())
        self.assertEqual(result["source_ids"], ["P02"])

    def test_travel_claim_fallback(self):
        result = answer_question("How much can staff claim for travel?")
        self.assertEqual(result["answer"], FALLBACK_ANSWER)
        self.assertEqual(result["source_ids"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
