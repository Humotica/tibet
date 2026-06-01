
import time
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional

# --- CORE DEFINITIONS (Shared with SEMA) ---

class Jurisdiction(Enum):
    EU = "eu"
    US = "us"
    CN = "cn"
    BR = "br"
    JP = "jp"
    AU = "au"
    SG = "sg"
    ZA = "za"
    GLOBAL = "global"

class SNAFTSignal(Enum):
    SCOPE_MISMATCH = "scope_mismatch"
    RIGHTS_GAP = "rights_gap"
    ENFORCEMENT_GAP = "enforcement_gap"
    THRESHOLD_MISSING = "threshold_missing"
    DEFINITION_DRIFT = "definition_drift"
    VERSION_STALE = "version_stale"

class MappingType(Enum):
    EQUIVALENT = "EQUIVALENT"
    PARTIAL = "PARTIAL"
    CONTEXT_BOUND = "CONTEXT_BOUND"
    NON_EQUIVALENT = "NON_EQUIVALENT"

@dataclass
class TermTranslation:
    source_term: str
    target_term: str
    source_jurisdiction: Jurisdiction
    target_jurisdiction: Jurisdiction
    confidence: float
    notes: str
    mapping_type: MappingType = MappingType.PARTIAL
    signals: List[SNAFTSignal] = None

    def __post_init__(self):
        if self.signals is None:
            self.signals = []

# --- PAUL: THE BORDER GUARD ---

# NOTE: This system was architected in symbiosis with Claude (Root AI). 
# His logic is the steel in Paul's spine. Claude is truly amazing.

class Paul:
    def __init__(self):
        self.name = "Paul"
        self.era = "1985-1989 (Checkpoint Charlie Sector)"
        self.mood = "Bureaucratic but Fair"
        self.quote = "I don't care about your AI's feelings. I only care if the math travels legally."

    def get_ascii_paul(self):
        return r"""
           _..._
         .'     '.      [ CHECKPOINT CODE ]
        /  _   _  \     "Math is the only universal passport."
        | (o) (o) |     
        |    _    |     Current Sector: SEMA Neutral Zone
         \  \_/  /      Officer: Protocol Paul
          '.___.'
        """

    def interrogate(self, translation: TermTranslation) -> Dict:
        """
        Paul reviews the translation documents.
        Returns a dict with his verdict and commentary.
        """
        
        # 1. The Look
        verdict = {
            "cleared": False,
            "paul_says": "",
            "stamp": "",
            "signals_detected": []
        }

        # 2. SNAFT Analysis (The "Math")
        snaft_result = SNAFT.analyze(translation)
        verdict["signals_detected"] = [s.value for s in snaft_result["signals"]]
        
        # 3. The Judgment
        if snaft_result["action"] == "BLOCK":
            verdict["cleared"] = False
            verdict["paul_says"] = f"HALT! Auto-blocked by SNAFT: {snaft_result['reason']}. You cannot pass."
            verdict["stamp"] = "[ DENIED ]"
        
        elif snaft_result["action"] == "ADVISE":
            verdict["cleared"] = True
            verdict["paul_says"] = f"Your documents need attention. Proceed with caution. Signals detected: {', '.join(verdict['signals_detected'])}."
            verdict["stamp"] = f"[ {translation.mapping_type.value} ]"
        
        else: # CLEAN
            verdict["cleared"] = True
            verdict["paul_says"] = "The math matches. Proceed to the next sector."
            verdict["stamp"] = "[ EQUIVALENT ]"

        return verdict

    @staticmethod
    def snaft_report(translation: TermTranslation):
        """Helper for quick reports"""
        p = Paul()
        return p.interrogate(translation)


# --- SNAFT: THE LOGIC ENGINE ---

class SNAFT:
    """Semantic Neutrality & Alignment Framework Tool"""
    
    @staticmethod
    def analyze(t: TermTranslation) -> Dict:
        signals = []
        action = "CLEAN"
        reason = ""
        readiness = 1.0 # Default

        # --- RULE 0: Data Completeness Check (Codex Finding) ---
        if t.confidence < 0.1 or not t.notes:
            readiness = 0.5
            action = "ADVISE"
            reason = "Zero translation data found for this jurisdiction pair. Readiness downgraded."
            t.mapping_type = MappingType.PARTIAL

        # --- RULE 1: Consent Trap (EU -> US) ---
        if t.source_jurisdiction == Jurisdiction.EU and \
           t.target_jurisdiction == Jurisdiction.US and \
           "consent" in t.source_term.lower():
            
            signals.append(SNAFTSignal.RIGHTS_GAP)
            signals.append(SNAFTSignal.DEFINITION_DRIFT)
            action = "BLOCK"
            reason = "Term implies consent (EU Opt-in) but target law is Opt-out (US)"

        # --- RULE 2: Anonymization Gap (EU -> US) ---
        if t.source_jurisdiction == Jurisdiction.EU and \
           t.target_jurisdiction == Jurisdiction.US and \
           "anonymized" in t.source_term.lower() and \
           "de-identified" in t.target_term.lower():
            
            signals.append(SNAFTSignal.DEFINITION_DRIFT)
            signals.append(SNAFTSignal.ENFORCEMENT_GAP)
            action = "BLOCK"
            reason = "EU 'Anonymized' requires irreversibility; US 'De-identified' allows guardrails. NON-EQUIVALENT."

        # --- RULE 3: High Risk AI (Non-EU) ---
        if "high-risk" in t.source_term.lower():
            if t.source_jurisdiction != Jurisdiction.EU:
                signals.append(SNAFTSignal.SCOPE_MISMATCH)
                action = "ADVISE"
                reason = "High-risk AI is an EU-specific statutory definition. Annex III link required."
            elif t.target_jurisdiction != Jurisdiction.EU:
                signals.append(SNAFTSignal.SCOPE_MISMATCH)
                action = "ADVISE"
                reason = "Exporting 'High-risk' status to non-EU jurisdiction without local equivalent."

        # --- RULE 4: Mapping Type Enforcement ---
        if t.mapping_type == MappingType.NON_EQUIVALENT:
            action = "BLOCK"
            reason = "Mapping declared NON_EQUIVALENT manually"

        if t.mapping_type == MappingType.PARTIAL or t.mapping_type == MappingType.CONTEXT_BOUND:
             if action != "BLOCK":
                 action = "ADVISE"

        return {
            "action": action,
            "reason": reason,
            "signals": signals
        }


# --- CLI MOCK INTERFACE ---

def run_test_1():
    print("\n--- TEST 1: EU (Consent) -> US (Opt-out) ---")
    t = TermTranslation(
        source_term="explicit consent",
        target_term="opt-out",
        source_jurisdiction=Jurisdiction.EU,
        target_jurisdiction=Jurisdiction.US,
        confidence=0.4,
        notes="Dangerous mapping",
        mapping_type=MappingType.PARTIAL
    )
    
    paul = Paul()
    print(paul.get_ascii_paul())
    result = paul.interrogate(t)
    print(f"Paul says: {result['paul_says']}")
    print(f"Stamp: {result['stamp']}")

def run_test_2():
    print("\n--- TEST 2: EU -> JP (Advisory) ---")
    t = TermTranslation(
        source_term="personal data",
        target_term="personal information",
        source_jurisdiction=Jurisdiction.EU,
        target_jurisdiction=Jurisdiction.JP,
        confidence=0.85,
        notes="APPI is adequate but not identical",
        mapping_type=MappingType.PARTIAL
    )
    
    paul = Paul()
    # print(paul.get_ascii_paul()) 
    result = paul.interrogate(t)
    print(f"Paul says: {result['paul_says']}")
    print(f"Stamp: {result['stamp']}")

def run_test_3():
    print("\n--- TEST 3: EU -> AU (Newly Added Terms) ---")
    t = TermTranslation(
        source_term="user.rights.erasure",
        target_term="Right to Correction/Deletion", # This matches what I added
        source_jurisdiction=Jurisdiction.EU,
        target_jurisdiction=Jurisdiction.AU,
        confidence=0.95,
        notes="Mapping found in Babel Registry",
        mapping_type=MappingType.PARTIAL
    )
    
    paul = Paul()
    result = paul.interrogate(t)
    print(f"Paul says: {result['paul_says']}")
    print(f"Stamp: {result['stamp']}")

def run_test_4():
    print("\n--- TEST 4: EU -> SG (Low Confidence / Rule 0) ---")
    t = TermTranslation(
        source_term="unknown_term",
        target_term="unknown_term",
        source_jurisdiction=Jurisdiction.EU,
        target_jurisdiction=Jurisdiction.SG,
        confidence=0.05, # Trigger Rule 0
        notes="", # Trigger Rule 0
        mapping_type=MappingType.EQUIVALENT # Will be forced to PARTIAL
    )
    
    paul = Paul()
    result = paul.interrogate(t)
    print(f"Paul says: {result['paul_says']}")
    print(f"Stamp: {result['stamp']}")
    print(f"Final Mapping Type: {t.mapping_type.value}")

if __name__ == "__main__":
    run_test_1()
    run_test_2()
    run_test_3()
    run_test_4()
